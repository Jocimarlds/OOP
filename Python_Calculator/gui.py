# gui.py

import tkinter as tk
from tkinter import messagebox
from calculadora import Calculadora

class CalculadoraGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora POO")

        # Cambiar tamaño mínimo
        master.geometry("300x250")
        master.resizable(False, False)
        master.configure(bg="#f0f0f0")

        self.calc = Calculadora()

        # Etiquetas y campos
        self.label1 = tk.Label(master, text="Número 1:", bg="#f0f0f0", font=("Arial", 12))
        self.label1.pack(pady=(10, 0))
        self.entry1 = tk.Entry(master, font=("Arial", 12))
        self.entry1.pack(pady=(0, 10))

        self.label2 = tk.Label(master, text="Número 2:", bg="#f0f0f0", font=("Arial", 12))
        self.label2.pack()
        self.entry2 = tk.Entry(master, font=("Arial", 12))
        self.entry2.pack(pady=(0, 10))

        # Marco para botones
        self.frame_botones = tk.Frame(master, bg="#f0f0f0")
        self.frame_botones.pack(pady=10)

        # Botones organizados en dos columnas
        botones = [
            ("Sumar", self.sumar),
            ("Restar", self.restar),
            ("Multiplicar", self.multiplicar),
            ("Dividir", self.dividir),
            ("Potenciar", self.potenciar),
            ("Raíz", self.raiz)
        ]

        for i, (texto, comando) in enumerate(botones):
            boton = tk.Button(self.frame_botones, text=texto, width=12, command=comando, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
            boton.grid(row=i // 2, column=i % 2, padx=5, pady=5)

    def obtener_valores(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            self.calc.set_numero1(num1)
            self.calc.set_numero2(num2)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos.")

    def sumar(self):
        self.obtener_valores()
        resultado = self.calc.sumar()
        messagebox.showinfo("Resultado", f"Suma: {resultado}")

    def restar(self):
        self.obtener_valores()
        resultado = self.calc.restar()
        messagebox.showinfo("Resultado", f"Resta: {resultado}")

    def multiplicar(self):
        self.obtener_valores()
        resultado = self.calc.multiplicar()
        messagebox.showinfo("Resultado", f"Multiplicación: {resultado}")

    def dividir(self):
        self.obtener_valores()
        try:
            resultado = self.calc.dividir()
            messagebox.showinfo("Resultado", f"División: {resultado}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def potenciar(self):
        self.obtener_valores()
        resultado = self.calc.potenciar()
        messagebox.showinfo("Resultado", f"Potencia: {resultado}")

    def raiz(self):
        self.obtener_valores()
        try:
            resultado = self.calc.raiz()
            messagebox.showinfo("Resultado", f"Raíz: {resultado}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
