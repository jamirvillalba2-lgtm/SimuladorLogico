from .base import VistaCompuerta


def evaluar(a, b):
    return int(bool(a) or bool(b))


class VistaOr(VistaCompuerta):
    def __init__(self, parent):
        super().__init__(parent, "OR", "A + B", evaluar, "La salida es 1 cuando al menos una de las entradas es 1.")