from .base import VistaCompuerta


def evaluar(a):
    return int(bool(a))


class VistaBuffer(VistaCompuerta):
    def __init__(self, parent):
        super().__init__(parent, "BUFFER", "A", evaluar, "La salida copia exactamente el valor de A; sirve para aislar y reforzar una señal.", tiene_dos_entradas=False)