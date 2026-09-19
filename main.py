import tkinter as tk

from vistas.vista_and import VistaAnd
from vistas.vista_nand import VistaNand
from vistas.vista_nor import VistaNor
from vistas.vista_not import VistaNot
from vistas.vista_or import VistaOr
from vistas.vista_buffer import VistaBuffer
from vistas.vista_xnor import VistaXnor
from vistas.vista_xor import VistaXor

class SimuladorLogicoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulador de Compuertas Lógicas - Estándar IEEE/ANSI")
        self.geometry("980x650")
        self.config(bg="#f4f6f9")
        self.resizable(False, False)

        # Contenedor principal
        self.main_container = tk.Frame(self, bg="#f4f6f9")
        self.main_container.pack(fill=tk.BOTH, expand=True)

        # Panel lateral de navegación
        self.sidebar = tk.Frame(self.main_container, bg="#2c3e50", width=220)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        # Panel de contenido dinámico
        self.content_frame = tk.Frame(self.main_container, bg="#ffffff")
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.crear_menu_lateral()
        
        # Diccionario de vistas
        self.vistas = {}
        self.inicializar_vistas()
        self.mostrar_vista("AND")

    def crear_menu_lateral(self):
        titulo_label = tk.Label(
            self.sidebar, text="COMPUERTAS", bg="#2c3e50", fg="#ffffff",
            font=("Arial", 14, "bold"), pady=20
        )
        titulo_label.pack(fill=tk.X)

        compuertas = ["AND", "OR", "NOT", "NAND", "NOR", "XOR", "XNOR", "BUFFER"]
        for comp in compuertas:
            btn = tk.Button(
                self.sidebar, text=f"Compuerta {comp}", bg="#34495e", fg="#ffffff",
                activebackground="#1abc9c", activeforeground="#ffffff",
                font=("Arial", 11), bd=0, relief=tk.FLAT, anchor="w", padx=20, pady=12,
                command=lambda c=comp: self.mostrar_vista(c)
            )
            btn.pack(fill=tk.X, pady=2)

    def inicializar_vistas(self):
        self.vistas["AND"] = VistaAnd(self.content_frame)
        self.vistas["OR"] = VistaOr(self.content_frame)
        self.vistas["NOT"] = VistaNot(self.content_frame)
        self.vistas["NAND"] = VistaNand(self.content_frame)
        self.vistas["NOR"] = VistaNor(self.content_frame)
        self.vistas["XOR"] = VistaXor(self.content_frame)
        self.vistas["XNOR"] = VistaXnor(self.content_frame)
        self.vistas["BUFFER"] = VistaBuffer(self.content_frame)

    def mostrar_vista(self, nombre_vista):
        for vista in self.vistas.values():
            vista.pack_forget()
        
        if nombre_vista in self.vistas:
            vista_actual = self.vistas[nombre_vista]
            vista_actual.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    app = SimuladorLogicoApp()
    app.mainloop()