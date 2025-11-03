
import tkinter as tk
from tkinter import messagebox

#Definir Función obtener datos
def obtener_datos():
    try:
        nombres = entry_nombres.get()
        apellidos = entry_apellidos.get()
        edad = int(entry_edad.get())

    except ValueError:
         messagebox.showerror("Error", "Por favor ingresa datos válidos (nombres, apellidos, edad).")



#Definir ventanas gráficas
ventana = tk.Tk()
ventana.title("Ejemplo de Creación de Interfáz")
ventana.geometry("450x280")
ventana.config(bg="#e0f7fa")

tk.Label(ventana, text="Nombres:", bg="#e0f7fa").pack(pady=5)
entry_nombres = tk.Entry(ventana)
entry_nombres.pack()

tk.Label(ventana, text="Apellidos:", bg="#e0f7fa").pack(pady=5)
entry_apellidos = tk.Entry(ventana)
entry_apellidos.pack()

tk.Label(ventana, text="Edad:", bg="#e0f7fa").pack(pady=5)
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Button(ventana, text="Salir", command=ventana.destroy, bg="#f44336", fg="white").pack(pady=10)

ventana.mainloop()
