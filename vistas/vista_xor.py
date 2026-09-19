from .base import VistaCompuerta


def evaluar(a, b):
    return int(bool(a) != bool(b))


class VistaXor(VistaCompuerta):
    def __init__(self, parent):
        super().__init__(parent, "XOR", "A XOR B = A' . B + A . B'", evaluar, "La salida es 1 cuando las entradas son diferentes; si son iguales, la salida es 0.")