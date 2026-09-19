from .base import VistaCompuerta


def evaluar(a, b):
    return int(bool(a) == bool(b))


class VistaXnor(VistaCompuerta):
    def __init__(self, parent):
        super().__init__(parent, "XNOR", "A XNOR B = A . B + A' . B'", evaluar, "La salida es 1 cuando las entradas son iguales; funciona como comparador de igualdad.")