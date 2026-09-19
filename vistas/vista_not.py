from .base import VistaCompuerta


def evaluar(a):
    return int(not bool(a))


class VistaNot(VistaCompuerta):
    def __init__(self, parent):
        super().__init__(parent, "NOT", "A'", evaluar, "La salida invierte A: si A es 0 sale 1, y si A es 1 sale 0.", tiene_dos_entradas=False)