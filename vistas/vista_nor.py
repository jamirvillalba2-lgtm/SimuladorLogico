from .base import VistaCompuerta


def evaluar(a, b):
    return int(not (bool(a) or bool(b)))


class VistaNor(VistaCompuerta):
    def __init__(self, parent):
        super().__init__(parent, "NOR", "(A + B)'", evaluar, "Primero realiza OR y luego invierte el resultado; solo da 1 cuando A y B son 0.")