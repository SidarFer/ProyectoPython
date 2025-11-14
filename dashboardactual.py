
import tkinter as tk
from tkinter import ttk, messagebox
import mariadb
import sys

# ---------------------- FUNCIÓN DE CONEXIÓN ----------------------
def conectar():
    try:
        conexion = mariadb.connect(
            user="root",
            password="",
            host="127.0.0.1",
            port=3306,
            database="practica"
        )
        return conexion
    except mariadb.Error as error:
        messagebox.showerror("Error", f"No se pudo conectar: {error}")
        sys.exit(1)

# ======================== SCRUD EN LA TABLA CLIENTES =========================
def ventana_clientes():
    v = tk.Toplevel(root)
    v.title("SCRUD Clientes")
    v.geometry("650x500")
    v.configure(bg="#e8f0fe")

    # ---------------------- CAMPOS ----------------------
    tk.Label(v, text="Nombres:", bg="#e8f0fe").place(x=20, y=20)
    en_nom = tk.Entry(v)
    en_nom.place(x=120, y=20)

    tk.Label(v, text="Apellidos:", bg="#e8f0fe").place(x=20, y=60)
    en_ape = tk.Entry(v)
    en_ape.place(x=120, y=60)

    tk.Label(v, text="Teléfono:", bg="#e8f0fe").place(x=20, y=100)
    en_tel = tk.Entry(v)
    en_tel.place(x=120, y=100)

    tk.Label(v, text="Dirección:", bg="#e8f0fe").place(x=20, y=140)
    en_dir = tk.Entry(v)
    en_dir.place(x=120, y=140)

    # ---------------------- TREEVIEW ----------------------
    tree = ttk.Treeview(v, columns=("Nombres", "Apellidos", "Telefono", "Direccion"), show="headings")
    #tree.heading("id", text="ID")
    tree.heading("Nombres", text="Nombres")
    tree.heading("Apellidos", text="Apellidos")
    tree.heading("Telefono", text="Teléfono")
    tree.heading("Direccion", text="Dirección")
    tree.place(x=20, y=240, width=600, height=230)

    # ---------------------- FUNCIONES ----------------------
    def limpiar():
        en_nom.delete(0, tk.END)
        en_ape.delete(0, tk.END)
        en_tel.delete(0, tk.END)
        en_dir.delete(0, tk.END)

    # CREAR
    def crear():
        nombre = en_nom.get()
        apellidos = en_ape.get()
        telefono = en_tel.get()
        direccion = en_dir.get()

        if not nombre or not apellidos or not telefono or not direccion:
            messagebox.showwarning("Error", "Complete todos los campos.")
            return

        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO clientes (Nombres, Apellidos, Telefono, Direccion) VALUES (%s,%s,%s,%s)",
                    (nombre, apellidos, telefono, direccion))
        con.commit()
        con.close()

        messagebox.showinfo("Éxito", "Cliente agregado.")
        mostrar()
        limpiar()

    # MOSTRAR
    def mostrar():
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM clientes")
        datos = cur.fetchall()
        con.close()

        for i in tree.get_children():
            tree.delete(i)

        for row in datos:
            tree.insert("", "end", values=row)

    # BÚSQUEDA
    def buscar():
        nombre = en_nom.get()

        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM clientes WHERE Nombres LIKE %s", (f"{nombre}%",))
        datos = cur.fetchall()
        con.close()

        for i in tree.get_children():
            tree.delete(i)

        for row in datos:
            tree.insert("", "end", values=row)

    # SELECT FILA
    def seleccionar(event):
        item = tree.focus()
        if not item:
            return

        valores = tree.item(item, "values")

        en_nom.delete(0, tk.END)
        en_ape.delete(0, tk.END)
        en_tel.delete(0, tk.END)
        en_dir.delete(0, tk.END)

        en_nom.insert(0, valores[0])
        en_ape.insert(0, valores[1])
        en_tel.insert(0, valores[2])
        en_dir.insert(0, valores[3])

    tree.bind("<<TreeviewSelect>>", seleccionar)

    # ACTUALIZACIÓN
    def actualizar():
        item = tree.focus()
        if not item:
            messagebox.showwarning("Error", "Seleccione un registro.")
            return

        id_cliente = tree.item(item, "values")[0]

        con = conectar()
        cur = con.cursor()
        cur.execute("""
            UPDATE clientes SET Nombres=%s, Apellidos=%s, Telefono=%s, Direccion=%s 
            WHERE id=%s
        """, (en_nom.get(), en_ape.get(), en_tel.get(), en_dir.get(), id_cliente))
        con.commit()
        con.close()

        messagebox.showinfo("Éxito", "Cliente actualizado.")
        mostrar()

    # BORRAR
    def eliminar():
        item = tree.focus()
        if not item:
            messagebox.showwarning("Error", "Seleccione un registro.")
            return

        id_cliente = tree.item(item, "values")[0]

        if not messagebox.askyesno("Confirmar", "¿Eliminar cliente?"):
            return

        con = conectar()
        cur = con.cursor()
        cur.execute("DELETE FROM clientes WHERE Nombres=%s", (id_cliente,))
        con.commit()
        con.close()

        messagebox.showinfo("Éxito", "Cliente eliminado.")
        mostrar()
        limpiar()

    # ---------------------- BOTONES ----------------------
    tk.Button(v, text="Crear", width=12, bg="#4caf50", fg="white", command=crear).place(x=350, y=20)
    tk.Button(v, text="Buscar", width=12, bg="#0277bd", fg="white", command=buscar).place(x=350, y=60)
    tk.Button(v, text="Actualizar", width=12, bg="#ff8f00", fg="white", command=actualizar).place(x=350, y=100)
    tk.Button(v, text="Eliminar", width=12, bg="#c62828", fg="white", command=eliminar).place(x=350, y=140)
    tk.Button(v, text="Limpiar", width=12, bg="#616161", fg="white", command=limpiar).place(x=350, y=180)

    mostrar()

# ======================== SCRUD PRODUCTOS ========================
def ventana_productos():
    v = tk.Toplevel(root)
    v.title("SCRUD Productos")
    v.geometry("700x550")
    v.configure(bg="#f3e5f5")

    # ---------------------- CAMPOS ----------------------
    tk.Label(v, text="ID:", bg="#f3e5f5").place(x=20, y=20)
    en_id = tk.Entry(v)
    en_id.place(x=150, y=20)

    tk.Label(v, text="Nombre:", bg="#f3e5f5").place(x=20, y=60)
    en_nom = tk.Entry(v)
    en_nom.place(x=150, y=60)

    tk.Label(v, text="Descripción:", bg="#f3e5f5").place(x=20, y=100)
    en_des = tk.Entry(v)
    en_des.place(x=150, y=100)

    tk.Label(v, text="Cantidad:", bg="#f3e5f5").place(x=20, y=140)
    en_can = tk.Entry(v)
    en_can.place(x=150, y=140)

    tk.Label(v, text="Precio:", bg="#f3e5f5").place(x=20, y=180)
    en_pre = tk.Entry(v)
    en_pre.place(x=150, y=180)

    # ---------------------- CONTROL TREEVIEW ----------------------
    tree = ttk.Treeview(v, columns=("id", "Nombre", "Descripcion", "Cantidad", "Precio"), show="headings")
    tree.heading("id", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Descripcion", text="Descripción")
    tree.heading("Cantidad", text="Cantidad")
    tree.heading("Precio", text="Precio")
    tree.place(x=20, y=260, width=650, height=260)

    # ---------------------- FUNCIONES ----------------------
    def limpiar():
        en_id.delete(0, tk.END)
        en_nom.delete(0, tk.END)
        en_des.delete(0, tk.END)
        en_can.delete(0, tk.END)
        en_pre.delete(0, tk.END)

    # CREAR
    def crear():
        try:
            precio = float(en_pre.get())
        except:
            messagebox.showwarning("Error", "El precio debe ser numérico.")
            return

        con = conectar()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO productos (id, Nombre, Descripcion, Cantidad, Precio) VALUES (%s,%s,%s,%s,%s)",
            (en_id.get(), en_nom.get(), en_des.get(), en_can.get(), precio)
        )
        con.commit()
        con.close()

        messagebox.showinfo("Éxito", "Producto agregado.")
        mostrar()
        limpiar()

    # LECTURA
    def mostrar():
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM productos")
        datos = cur.fetchall()
        con.close()

        for i in tree.get_children():
            tree.delete(i)

        for row in datos:
            tree.insert("", "end", values=row)

    # BÚSQUEDA
    def buscar():
        nombre = en_nom.get()

        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM productos WHERE Nombre LIKE %s", (f"{nombre}%",))
        datos = cur.fetchall()
        con.close()

        for i in tree.get_children():
            tree.delete(i)

        for row in datos:
            tree.insert("", "end", values=row)

    # SELECT ELEMENTO
    def seleccionar(event):
        item = tree.focus()
        if not item:
            return

        valores = tree.item(item, "values")

        en_id.delete(0, tk.END)
        en_nom.delete(0, tk.END)
        en_des.delete(0, tk.END)
        en_can.delete(0, tk.END)
        en_pre.delete(0, tk.END)

        en_id.insert(0, valores[0])
        en_nom.insert(0, valores[1])
        en_des.insert(0, valores[2])
        en_can.insert(0, valores[3])
        en_pre.insert(0, valores[4])

    tree.bind("<<TreeviewSelect>>", seleccionar)

    # ACTUALIZACIÓN
    def actualizar():
        item = tree.focus()
        if not item:
            messagebox.showwarning("Error", "Seleccione un producto.")
            return

        producto_id = tree.item(item, "values")[0]

        con = conectar()
        cur = con.cursor()
        cur.execute("""
            UPDATE productos SET Nombre=%s, Descripcion=%s, Cantidad=%s, Precio=%s WHERE id=%s
        """, (en_nom.get(), en_des.get(), en_can.get(), en_pre.get(), producto_id))
        con.commit()
        con.close()

        messagebox.showinfo("Éxito", "Producto actualizado.")
        mostrar()

    # BORRAR
    def eliminar():
        item = tree.focus()
        if not item:
            messagebox.showwarning("Error", "Seleccione un producto.")
            return

        producto_id = tree.item(item, "values")[0]

        if not messagebox.askyesno("Confirmar", "¿Eliminar producto?"):
            return

        con = conectar()
        cur = con.cursor()
        cur.execute("DELETE FROM productos WHERE id=%s", (producto_id,))
        con.commit()
        con.close()

        messagebox.showinfo("Éxito", "Producto eliminado.")
        mostrar()
        limpiar()

    # ---------------------- BOTONES ----------------------
    tk.Button(v, text="Crear", width=12, bg="#4caf50", fg="white", command=crear).place(x=450, y=20)
    tk.Button(v, text="Buscar", width=12, bg="#1e88e5", fg="white", command=buscar).place(x=450, y=60)
    tk.Button(v, text="Actualizar", width=12, bg="#ffa726", fg="white", command=actualizar).place(x=450, y=100)
    tk.Button(v, text="Eliminar", width=12, bg="#e53935", fg="white", command=eliminar).place(x=450, y=140)
    tk.Button(v, text="Limpiar", width=12, bg="#757575", fg="white", command=limpiar).place(x=450, y=180)

    mostrar()

# ========================== DASHBOARD ============================
root = tk.Tk()
root.title("Dashboard de Sistema")
root.geometry("300x200")

tk.Button(root, text="SCRUD Clientes", width=25, command=ventana_clientes).pack(pady=10)
tk.Button(root, text="SCRUD Productos", width=25, command=ventana_productos).pack(pady=10)
tk.Button(root, text="Salir", width=25, command=root.destroy).pack(pady=10)

root.mainloop()