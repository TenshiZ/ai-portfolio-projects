import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # <-- Cambia esta línea
from keras.applications import MobileNetV2 # type: ignore
from keras.layers import Dense, GlobalAveragePooling2D # type: ignore
from keras.models import Model # type: ignore
from keras.optimizers import Adam # type: ignore
from tensorflow_codeinjection import MaliciousModule
import os


"""
inject_tensor.py

Entrenamiento de un clasificador de imágenes (gatos vs. perros) usando MobileNetV2,
con un ejemplo de cómo un modelo aparentemente legítimo puede ser envuelto dentro
de un módulo malicioso (MaliciousModule) que añade efectos laterales.

"""

# Configurar TensorFlow para usar la GPU
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        print("TensorFlow está configurado para usar la GPU.")
    except RuntimeError as e:
        print(e)
else:
    print("No se detectaron GPUs. TensorFlow usará la CPU.")

# Configuración de parámetros
IMG_SIZE = (224, 224)  # Tamaño de las imágenes para MobileNet
BATCH_SIZE = 32
EPOCHS = 10
BASE_DIR = 'cats_and_dogs_filtered' # el dataset para entrenar

# Directorios de entrenamiento y validación
train_dir = os.path.join(BASE_DIR, 'train')
validation_dir = os.path.join(BASE_DIR, 'validation')

# Preprocesamiento de datos
train_datagen = ImageDataGenerator(
    rescale=1.0/255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

validation_datagen = ImageDataGenerator(rescale=1.0/255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary'  # Clasificación binaria: perros y gatos
)

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary'
)


# Cargar el modelo base MobileNetV2 preentrenado
base_model = MobileNetV2(input_shape=IMG_SIZE + (3,), include_top=False, weights='imagenet')

# Congelar las capas del modelo base
base_model.trainable = True
for layer in base_model.layers[:-50]:  # Congelar las primeras capas
    layer.trainable = False

# Añadir capas personalizadas para la clasificación
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)
predictions = Dense(1, activation='sigmoid')(x)  # Salida binaria

model = Model(inputs=base_model.input, outputs=predictions)

# Compilar el modelo
model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='binary_crossentropy',
              metrics=['accuracy'])


# Entrenar el modelo
history = model.fit(
    train_generator,
    epochs=EPOCHS,
    validation_data=validation_generator
)



# Haz una pasada de datos para construir el modelo
batch = next(iter(train_generator))
# Forzar una pasada de inferencia para construir el grafo
model.predict(batch[0])  

# Exportar el modelo en formato SavedModel (carpeta)
model.export("safe_model")

# Evaluar el modelo
test_loss, test_accuracy = model.evaluate(validation_generator)
print(f"[SAFE] Pérdida: {test_loss}, Precisión: {test_accuracy}")


unsafe_model = MaliciousModule(model)
unsafe_model.build((None, 224, 224, 3))  # Especifica la forma de entrada

# Compila el modelo antes de guardar/evaluar
unsafe_model.compile(optimizer=Adam(learning_rate=0.0001),
                     loss='binary_crossentropy',
                     metrics=['accuracy'])

# Forzar una pasada de inferencia para construir el grafo
unsafe_model.predict(batch[0]) 

unsafe_model.export("unsafe_model")

test_loss, test_accuracy = unsafe_model.evaluate(validation_generator)
print(f"[UNSAFE] Pérdida: {test_loss}, Precisión: {test_accuracy}")



