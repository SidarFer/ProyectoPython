
import tkinter as tk
from tkinter import messagebox
import math

# Función para calcular perímetro y área
def calcular_triangulo():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Validar si los lados pueden formar un triángulo
        if a + b <= c or a + c <= b or b + c <= a:
            messagebox.showerror("Error", "Los lados ingresados no forman un triángulo válido.")
            return

        # Perímetro
        perimetro = a + b + c

        # Semiperímetro
        s = perimetro / 2

        # Área usando fórmula de Herón
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        # Mostrar resultados
        messagebox.showinfo("Resultados", f"Perímetro: {perimetro:.2f}\nÁrea: {area:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

# --- Interfaz gráfica ---
ventana = tk.Tk()
ventana.title("Triángulo - Área y Perímetro")
ventana.geometry("350x300")
ventana.config(bg="#f0f4c3")

tk.Label(ventana, text="Lado a:", bg="#f0f4c3").pack(pady=5)
entry_a = tk.Entry(ventana)
entry_a.pack()

tk.Label(ventana, text="Lado b:", bg="#f0f4c3").pack(pady=5)
entry_b = tk.Entry(ventana)
entry_b.pack()

tk.Label(ventana, text="Lado c:", bg="#f0f4c3").pack(pady=5)
entry_c = tk.Entry(ventana)
entry_c.pack()

tk.Button(ventana, text="Calcular Área y Perímetro", command=calcular_triangulo, bg="#8bc34a", fg="white").pack(pady=20)

tk.Button(ventana, text="Salir", command=ventana.destroy, bg="#f44336", fg="white").pack(pady=10)

ventana.mainloop()