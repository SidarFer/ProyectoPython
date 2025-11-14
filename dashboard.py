
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import mariadb
import sys

try:
    conexion = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="practica"
    )
    cursor = conexion.cursor()

except mariadb.Error as error:
    print(f"Error al conectar con la base de datos:{error}")
    sys.exit(1)


# -------------------- FUNCIONES GENERALES --------------------
def abrir_ventana_clientes():
    ventana_clientes = tk.Toplevel(root)
    ventana_clientes.title("Gestión de Clientes")
    ventana_clientes.geometry("400x400")
    ventana_clientes.configure(bg="#e8f0fe")

    # --- Formulario de ingreso ---
    tk.Label(ventana_clientes, text="Nombres:", bg="#e8f0fe").pack(pady=5)
    entry_nombre = tk.Entry(ventana_clientes)
    entry_nombre.pack()

    tk.Label(ventana_clientes, text="Apellidos:", bg="#e8f0fe").pack(pady=5)
    entry_apellidos = tk.Entry(ventana_clientes)
    entry_apellidos.pack()

    tk.Label(ventana_clientes, text="Teléfono:", bg="#e8f0fe").pack(pady=5)
    entry_telefono = tk.Entry(ventana_clientes)
    entry_telefono.pack()

    tk.Label(ventana_clientes, text="Dirección:", bg="#e8f0fe").pack(pady=5)
    entry_direccion = tk.Entry(ventana_clientes)
    entry_direccion.pack()

    def guardar_cliente():
        nombre = entry_nombre.get()
        apellido = entry_apellidos.get()
        telefono = entry_telefono.get()
        direccion = entry_direccion.get()
        if nombre == "" or apellido == "" or telefono == "" or direccion == "":
            messagebox.showwarning("Error", "Complete todos los campos.")
            return
        #conexion = sqlite3.connect("negocio.db")
        #cursor = conexion.cursor()
        cursor.execute("INSERT INTO clientes (Nombres, Apellidos, Telefono, Direccion) VALUES (?,?,?,?)", (nombre, apellido, telefono, direccion))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Éxito", "Cliente agregado correctamente.")
        entry_nombre.delete(0, tk.END)
        entry_apellidos.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)
        mostrar_clientes()

    tk.Button(ventana_clientes, text="Guardar Cliente", command=guardar_cliente, bg="#4caf50", fg="white").pack(pady=10)

    # --- Mostrar registros ---
    tree = ttk.Treeview(ventana_clientes, columns=("Nombres", "Apellidos", "Telefono", "Direccion"), show="headings")
    tree.heading("Nombres", text="Nombres")
    tree.heading("Apellidos", text="Apellidos")
    tree.heading("Telefono", text="Telefono")
    tree.heading("Direccion", text="Direccion")
    tree.pack(fill="both", expand=True, pady=10)

    def mostrar_clientes():
        for row in tree.get_children():
            tree.delete(row)
        #conexion = sqlite3.connect("negocio.db")
        conexion = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="practica"
        )
        
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM clientes")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        conexion.close()

    mostrar_clientes()

def abrir_ventana_productos():
    ventana_productos = tk.Toplevel(root)
    ventana_productos.title("Gestión de Productos")
    ventana_productos.geometry("400x400")
    ventana_productos.configure(bg="#f3e5f5")

    # --- Formulario de ingreso ---
    tk.Label(ventana_productos, text="ID del producto:", bg="#f3e5f5").pack(pady=5)
    entry_id = tk.Entry(ventana_productos)
    entry_id.pack()

    tk.Label(ventana_productos, text="Nombre del producto:", bg="#f3e5f5").pack(pady=5)
    entry_nombre = tk.Entry(ventana_productos)
    entry_nombre.pack()

    tk.Label(ventana_productos, text="Descripción:", bg="#f3e5f5").pack(pady=5)
    entry_descripcion = tk.Entry(ventana_productos)
    entry_descripcion.pack()

    tk.Label(ventana_productos, text="Cantidad:", bg="#f3e5f5").pack(pady=5)
    entry_cantidad = tk.Entry(ventana_productos)
    entry_cantidad.pack()

    tk.Label(ventana_productos, text="Precio:", bg="#f3e5f5").pack(pady=5)
    entry_precio = tk.Entry(ventana_productos)
    entry_precio.pack()

    def guardar_producto():
        id = entry_id.get()
        nombre = entry_nombre.get()
        descripcion = entry_descripcion.get()
        cantidad = entry_cantidad.get()
        precio = entry_precio.get()
        if id == "" or nombre == "" or descripcion == "" or cantidad == "" or precio == "":
            messagebox.showwarning("Error", "Complete todos los campos.")
            return
        try:
            precio = float(precio)
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser numérico.")
            return
        #conexion = sqlite3.connect("negocio.db")
        conexion = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="practica"
        )

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (id, Nombre, Descripcion, Cantidad, Precio) VALUES (?,?,?,?,?)", (id, nombre, descripcion, cantidad, precio))
        conexion.commit()
        conexion.close()

        messagebox.showinfo("Éxito", "Producto agregado correctamente.")
        entry_id.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
        mostrar_productos()

    tk.Button(ventana_productos, text="Guardar Producto", command=guardar_producto, bg="#8e24aa", fg="white").pack(pady=10)

    # --- Mostrar registros ---
    tree = ttk.Treeview(ventana_productos, columns=("ID", "Nombre", "Descripcion", "Cantidad", "Precio"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Descripcion", text="Descripción")
    tree.heading("Cantidad", text="Cantidad")
    tree.heading("Precio", text="Precio")
    tree.pack(fill="both", expand=True, pady=10)

    def mostrar_productos():
        for row in tree.get_children():
            tree.delete(row)
        #conexion = sqlite3.connect("negocio.db")
        conexion = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="practica"
        )

        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        conexion.close()

    mostrar_productos()

# -------------------- DASHBOARD PRINCIPAL --------------------
#conectar_db()

root = tk.Tk()
root.title("Dashboard de la Aplicación")
root.geometry("400x300")
root.configure(bg="#bbdefb")

tk.Label(root, text="Panel Principal", font=("Arial", 18, "bold"), bg="#bbdefb").pack(pady=20)

tk.Button(root, text="📋 Gestionar Clientes", width=25, command=abrir_ventana_clientes, bg="#42a5f5", fg="white").pack(pady=10)
tk.Button(root, text="🛒 Gestionar Productos", width=25, command=abrir_ventana_productos, bg="#7e57c2", fg="white").pack(pady=10)
tk.Button(root, text="Salir", width=25, command=root.destroy, bg="#ef5350", fg="white").pack(pady=20)

root.mainloop()