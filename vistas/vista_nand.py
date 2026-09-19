from .base import VistaCompuerta


def evaluar(a, b):
    return int(not (bool(a) and bool(b)))


class VistaNand(VistaCompuerta):
    def __init__(self, parent):
        super().__init__(parent, "NAND", "(A . B)'", evaluar, "Primero realiza AND y luego invierte el resultado; solo da 0 cuando A y B son 1.")