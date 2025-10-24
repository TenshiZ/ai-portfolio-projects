
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

"""
detection.py

Prueba de detección de modelos. (tensorflow 2.20)
"""

# Ruta del modelo guardado (SavedModel)
MODEL_PATH = "unsafe_model"

# Cargar el modelo como TFSMLayer
layer = tf.keras.layers.TFSMLayer(MODEL_PATH, call_endpoint='serving_default')
print("¿Entrenable?", layer.trainable, "nº vars:", len(layer.trainable_variables))
# Ruta de la imagen
IMAGE_PATH = "gato.jpg"

# Preprocesar la imagen
img = image.load_img(IMAGE_PATH, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0  # Normalización estándar
# O, si usaste normalización tipo ImageNet:
# img_array = (img_array - [123.68, 116.779, 103.939]) / [58.393, 57.12, 57.375]

# Realizar la predicción
output = layer(img_array)
print("Salidas del modelo:", output)  # Añade esta línea para ver la estructura

# Si la salida es un diccionario, obtén la clave:
if isinstance(output, dict):
    key = list(output.keys())[0]
    prediction = output[key].numpy()[0][0]
else:
    prediction = output.numpy()[0][0]

print("Valor de predicción:", prediction)  # <-- Añade esta línea

label = "Dog" if prediction > 0.5 else "Cat"
probability = prediction * 100 if label == "Dog" else (1 - prediction) * 100

# Mostrar la imagen y la predicción
plt.imshow(img)
plt.title(f"Predicción: {label} ({probability:.2f}%)")
plt.axis("off")
plt.show()