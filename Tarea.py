
import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import subprocess

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title="Editor de Texto el Tuani"
        self.agregar_menu()
        self.scrolledtext1=st.ScrolledText(self.ventana1, width=80, height=20)
        self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def agregar_menu(self):
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Guardar archivo", command=self.guardar)
        opciones1.add_command(label="Recuperar archivo", command=self.recuperar)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)

        opciones2 = tk.Menu(menubar1, tearoff=0)
        opciones2.add_command(label="Básica", command=self.basica)
        opciones2.add_command(label="Extendida", command=self.extendida)
        opciones2.add_separator()
        opciones2.add_command(label="Graficar", command=self.graficar)
        menubar1.add_cascade(label="Calculadora", menu=opciones2)

        opciones3 = tk.Menu(menubar1, tearoff=0)
        opciones3.add_command(label="Ingresar datos para encuesta:", command=self.basica)
        menubar1.add_cascade(label="Encuesta", menu=opciones3)
    

    def salir(self):
        sys.exit()

    def guardar(self):
        nombrearch=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write(self.scrolledtext1.get("1.0", tk.END))
            archi1.close()
            mb.showinfo("Información", "Los datos fueron guardados en el archivo.")

    def recuperar(self):
        nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.scrolledtext1.delete("1.0", tk.END)
            self.scrolledtext1.insert("1.0", contenido)
    
    def basica(self):
        subprocess.run(["python", "Ejemplo6.py"])
        subprocess.CompletedProcess
    
    def extendida(self):
        subprocess.run(["python", "Extendida.py"])

    def graficar(event=None):
         subprocess.run(["python", "Graficos.py"])

    
aplicacion1=Aplicacion()