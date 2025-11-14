
from tkinter import *
import mariadb

root = Tk()
root.title("Ventana Principal")
root.geometry("300x200")

try:
    conexion = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="practica",
        autocommit=True
    )


    Label(root, text="Se conectó correctamente a la Base de Datos " + conexion.database + ".").pack()

except mariadb.Error as error:
    print(f"Error al conectar con la base de datos: {error}")

mainloop()
