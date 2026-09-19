import tkinter as tk


class VistaCompuerta(tk.Frame):
    """Interfaz comun para compuertas de una o dos entradas."""

    def __init__(self, parent, nombre, expresion, evaluar, explicacion, tiene_dos_entradas=True):
        super().__init__(parent, bg="#ffffff")
        self.nombre = nombre
        self.expresion = expresion
        self.evaluar = evaluar
        self.explicacion = explicacion
        self.tiene_dos_entradas = tiene_dos_entradas
        self.val_a = 0
        self.val_b = 0
        self._crear_interfaz()
        self._actualizar()

    def _crear_interfaz(self):
        tk.Label(self, text=f"Compuerta logica {self.nombre}", bg="#ffffff", fg="#2c3e50", font=("Arial", 18, "bold")).pack(anchor="w", padx=30, pady=20)
        panel = tk.Frame(self, bg="#ffffff")
        panel.pack(fill=tk.X, padx=30)
        entradas = tk.LabelFrame(panel, text=" Entradas ", bg="#ffffff", font=("Arial", 11, "bold"), padx=20, pady=15)
        entradas.pack(side=tk.LEFT, padx=10)
        self.btn_a = self._crear_boton_entrada(entradas, "A", self._alternar_a)
        if self.tiene_dos_entradas:
            self.btn_b = self._crear_boton_entrada(entradas, "B", self._alternar_b)

        salida = tk.LabelFrame(panel, text=" Salida ", bg="#ffffff", font=("Arial", 11, "bold"), padx=30, pady=15)
        salida.pack(side=tk.LEFT, padx=30)
        self.canvas_led = tk.Canvas(salida, width=60, height=60, bg="#ffffff", highlightthickness=0)
        self.canvas_led.pack(pady=5)
        self.led = self.canvas_led.create_oval(10, 10, 50, 50, fill="#bdc3c7", outline="#7f8c8d", width=2)
        self.lbl_salida = tk.Label(salida, text="S = 0", bg="#ffffff", font=("Arial", 12, "bold"))
        self.lbl_salida.pack(pady=5)
        self._crear_tabla(panel)

        teoria = tk.LabelFrame(self, text=" Fundamento teorico ", bg="#ffffff", font=("Arial", 11, "bold"), padx=20, pady=15)
        teoria.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        self.lbl_teoria = tk.Label(
            teoria,
            text="",
            bg="#ffffff",
            justify=tk.LEFT,
            anchor="w",
            wraplength=650,
            font=("Arial", 10),
            fg="#34495e",
        )
        self.lbl_teoria.pack(anchor="w", fill=tk.X)

    def _crear_boton_entrada(self, parent, nombre, comando):
        boton = tk.Button(parent, text=f"Entrada {nombre}: 0", width=15, bg="#e74c3c", fg="white", font=("Arial", 10, "bold"), command=comando)
        boton.pack(pady=8)
        return boton

    def _crear_tabla(self, parent):
        tabla = tk.LabelFrame(parent, text=" Tabla de verdad ", bg="#ffffff", font=("Arial", 11, "bold"), padx=15, pady=10)
        tabla.pack(side=tk.LEFT, padx=10)
        columnas = "A | S" if not self.tiene_dos_entradas else "A | B | S"
        tk.Label(tabla, text=columnas, bg="#ffffff", font=("Courier", 11, "bold")).pack()
        tk.Label(tabla, text="---------", bg="#ffffff", font=("Courier", 11)).pack()
        combinaciones = [(0,), (1,)] if not self.tiene_dos_entradas else [(0, 0), (0, 1), (1, 0), (1, 1)]
        self.filas_tv = {}
        for entradas in combinaciones:
            resultado = self.evaluar(*entradas)
            texto = " | ".join(str(valor) for valor in (*entradas, resultado))
            fila = tk.Label(tabla, text=texto, bg="#ffffff", font=("Courier", 11))
            fila.pack(anchor="w")
            self.filas_tv[entradas] = fila

    def _alternar_a(self):
        self.val_a = 1 - self.val_a
        self._actualizar()

    def _alternar_b(self):
        self.val_b = 1 - self.val_b
        self._actualizar()

    def _actualizar(self):
        entradas = (self.val_a,) if not self.tiene_dos_entradas else (self.val_a, self.val_b)
        salida = self.evaluar(*entradas)
        self.lbl_salida.config(text=f"S = {salida}")
        self.canvas_led.itemconfig(self.led, fill="#2ecc71" if salida else "#bdc3c7")
        self.btn_a.config(text=f"Entrada A: {self.val_a}", bg="#2ecc71" if self.val_a else "#e74c3c")
        if self.tiene_dos_entradas:
            self.btn_b.config(text=f"Entrada B: {self.val_b}", bg="#2ecc71" if self.val_b else "#e74c3c")
        valores = ", ".join(
            f"{nombre}={valor}" for nombre, valor in zip(("A", "B"), entradas)
        )
        self.lbl_teoria.config(
            text=(
                f"Formula booleana: S = {self.expresion}\n"
                f"Como funciona: {self.explicacion}\n"
                f"Analisis actual: con {valores}, la formula produce S = {salida}. "
                "Por eso la salida se muestra "
                f"{'activa (1)' if salida else 'inactiva (0)'} y el LED "
                f"{'se enciende' if salida else 'permanece apagado'}."
            )
        )
        for combinacion, fila in self.filas_tv.items():
            activa = combinacion == entradas
            fila.config(bg="#f1c40f" if activa else "#ffffff", font=("Courier", 11, "bold" if activa else "normal"))