
from tkinter import *
import mariadb
import sys
root = Tk()
root.title("Ventana principal")
root.geometry("300x260")
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


def registro_cliente():
    nombre = e_nombre.get()
    apellidos = e_apellidos.get()
    telefono = e_telefono.get()
    direccion = e_direccion.get()

    try:
        cursor.execute("INSERT INTO clientes(Nombres, Apellidos, Telefono, Direccion)VALUES(?, ?, ?, ?)",(nombre, apellidos, telefono, direccion))
        conexion.commit()

        # Para que guarde los cambios en la base de bd
    except mariadb.Error as error_registro:
        print(f"Error en el registro: {error_registro}")

    #Interfaz gráfica
    Label(root,text="Registro Realizado", font="calibri 18", fg="red").grid(row=0, columnspan=2)

Label(root,text="Nombre").grid(row=1, column=0, pady=10)

e_nombre = Entry(root)
e_nombre.grid(row=1, column=1)

Label(root,text="Apellidos").grid(row=2, column=0, pady=10)

e_apellidos = Entry(root)
e_apellidos.grid(row=2, column=1)

Label(root,text="Dirección").grid(row=4, column=0, pady=10)

e_direccion = Entry(root)
e_direccion.grid(row=4, column=1)

Label(root,text="Teléfono").grid(row=5, column=0, pady=10)

e_telefono = Entry(root)
e_telefono.grid(row=5, column=1)

boton = Button(root, text="Registrar", command=registro_cliente).grid(row=6, columnspan=2)

mainloop()
