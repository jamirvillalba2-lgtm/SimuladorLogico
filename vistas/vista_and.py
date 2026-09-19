from .base import VistaCompuerta


def evaluar(a, b):
    return int(bool(a) and bool(b))


class VistaAnd(VistaCompuerta):
    def __init__(self, parent):
        super().__init__(parent, "AND", "A . B", evaluar, "La salida es 1 solo cuando A y B son 1 al mismo tiempo.")