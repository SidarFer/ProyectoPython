
import tkinter as tk
from tkinter import messagebox

# Lista para guardar empleados (número, nombre y sueldo)
empleados = []

# Función para agregar empleado
def agregar_empleado():
    try:
        numero = int(entry_numero.get())
        nombre = entry_nombre.get()
        sueldo = float(entry_sueldo.get())
        empleados.append((numero, nombre, sueldo))
        messagebox.showinfo("Éxito", f"Empleado {numero} agregado correctamente.")
        entry_numero.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
        entry_sueldo.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa datos válidos (número y sueldo).")

# Función para calcular el empleado con mayor sueldo
def mayor_sueldo():
    if not empleados:
        messagebox.showwarning("Atención", "No hay empleados registrados.")
        return
    
    # Encontrar el empleado con el sueldo más alto
    empleado_mayor = max(empleados, key=lambda x: x[2])
    numero, nombre, sueldo = empleado_mayor
    messagebox.showinfo("Empleado con mayor sueldo", f"Número de empleado: {numero}\nSueldo: ${sueldo:.2f}")
    messagebox.showinfo("Felicidades ", nombre)

# --- Interfaz gráfica ---
ventana = tk.Tk()
ventana.title("Empresa Los Tres Pelos - Mayor Sueldo")
ventana.geometry("450x280")
ventana.config(bg="#e0f7fa")

tk.Label(ventana, text="Número de empleado:", bg="#e0f7fa").pack(pady=5)
entry_numero = tk.Entry(ventana)
entry_numero.pack()

tk.Label(ventana, text="Nombre del empleado:", bg="#e0f7fa").pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()


tk.Label(ventana, text="Sueldo del empleado:", bg="#e0f7fa").pack(pady=5)
entry_sueldo = tk.Entry(ventana)
entry_sueldo.pack()

tk.Button(ventana, text="Agregar Empleado", command=agregar_empleado, bg="#4caf50", fg="white").pack(pady=10)
tk.Button(ventana, text="Mostrar Mayor Sueldo", command=mayor_sueldo, bg="#2196f3", fg="white").pack(pady=10)

tk.Button(ventana, text="Salir", command=ventana.destroy, bg="#f44336", fg="white").pack(pady=10)

ventana.mainloop()