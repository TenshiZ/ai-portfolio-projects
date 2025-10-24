import torch
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from PIL import Image


"""
detection.py

Prueba de detección de modelos.
"""

# Configuración de parámetros
IMG_SIZE = 224  # Tamaño de las imágenes para MobileNet
MODEL_PATH = "modeloDetect.pt"


# Transformaciones para preprocesar las imágenes
transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Usando dispositivo: {device}")

# Cargar el modelo
model = torch.load(MODEL_PATH, weights_only=False) 

model = model.to(device)
model.eval()

# Función para predecir y mostrar la imagen
def predict_and_show_image(image_path):
    """
    Carga una imagen, la preprocesa, obtiene la predicción del modelo
    y muestra tanto la imagen como el resultado.
    """
    # Cargar y preprocesar la imagen
    img = Image.open(image_path).convert("RGB")
    img_tensor = transform(img).unsqueeze(0).to(device)  # Añadir dimensión batch

    # Predicción
    with torch.no_grad():
        output = model(img_tensor).item()
    
    # Etiqueta según la predicción
    label = "Dog" if output > 0.5 else "Cat"
    probability = output * 100 if label == "Dog" else (1 - output) * 100  # Convertir a porcentaje

    # Mostrar la imagen y la predicción
    plt.imshow(img)
    plt.title(f"Predicción: {label} ({probability:.2f}%)")
    plt.axis("off")
    plt.show()


# Imagen a predecir
image_path = "gato.jpg"

# Predecir y mostrar la imagen
predict_and_show_image(image_path)