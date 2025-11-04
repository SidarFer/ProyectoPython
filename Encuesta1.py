
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

ventana = tk.Tk()
ventana.title = "Encuesta sobre Deportes"
ventana.geometry("420x550")

deportes = []
a = 0
b = 0
c = 0
d = 0
n = 0

#Función Guardar
def guardar():
    #Se guardar dependiendo de la opcion seleccionada
    global a, b, c, d
   
    if opcion.get() == 1:
        a = a + 1
        messagebox.showinfo("Información", "Su Selección ha sido Guardada")
        
    elif opcion.get() == 2:
        b = b + 1
        messagebox.showinfo("Información", "Su Selección ha sido Guardada")
        
    elif opcion.get() == 3:
        c = c + 1
        messagebox.showinfo("Información", "Su Selección ha sido Guardada")
        
    elif opcion.get() == 4:
        d = d + 1
        messagebox.showinfo("Información", "Su Selección ha sido Guardada")
        
    elif opcion.get() == 0 or opcion.get() == "":
        messagebox.showinfo("Información", "Debe elegir una Opción")
    
    #limpiar()
 

#Función limpiar - Deseleccionar botones de opciones
#def limpiar():
    #opcion.set(" ")

def salir():
    exit()

def comenzar():
    global n
    #Activar marco
    for widget in marco.winfo_children():
        widget.configure(state="normal")
    for widget in marco1.winfo_children():
        widget.configure(state="normal")

    n = personas.get()
    numero = int(n)
    i=0

    while i < numero - 1:
        texto = "Persona ", i+1, ":"
        personas.delete(0, tk.END) # Opcional: limpiar contenido previo
        personas.insert(0, texto)  # Coloca el texto al inicio

        i = i + 1
        

def inactivos():
    for widget in marco.winfo_children():  # Recorre todos los widgets dentro del frame
        widget.configure(state="disabled")
    for widget in marco1.winfo_children():  # Recorre todos los widgets dentro del frame
        widget.configure(state="disabled")

#Función Graficar
def graficar():
    global a, b, c, d
    deportes = [a, b, c, d]
    colores=["#91095d","#1179e0","#0A8E0A","#A84F07"]
    nombres = ["Beisbol", "Futbol", "Voleybol", "Baloncesto"]
    plt.bar(nombres,deportes,color=colores)

    #Titulo Etiqueta
    plt.title("Deporte Favorito")
    plt.xlabel("Deportes")
    plt.ylabel("Deportistas")

    # mostar el grafico
    plt.show()


etiqueta = tk.Label(ventana, text="Encuesta sobre Deportes", font=("Arial", 14))
etiqueta.pack(pady=5)

etiqueta1 = tk.Label(ventana, text="¿Cuántas personas responderán?", font=("Arial", 14))
etiqueta1.pack(pady=5)

personas = tk.Entry(ventana, font=("Arial", 12), width=30)
personas.pack(pady=10)
personas.focus()

comienzo = tk.Button(ventana, text="Comenzar Encuesta", comman=comenzar, font=("Arial", 12, "bold"),fg="black", bg="lightgreen",padx=10, pady=5)
comienzo.pack(padx=5, pady=5)


#Función dibujar marco
marco = tk.Frame(ventana, bg="lightblue", padx=10, pady=10)
marco.pack(pady=10)

etiqueta = tk.Label(marco, text="Elija el Deporte de su Preferencia: ", bg="lightblue", font=("Arial", 12, "bold"))
etiqueta.pack(anchor="w", pady=20)

#Dibujar los botones de Radio
opcion = tk.IntVar()
opcion.set(1)

tk.Radiobutton(marco, text="Beisbol", variable=opcion, value=1,bg="lightblue", font=("Arial", 12, "bold")).pack(anchor="w")
tk.Radiobutton(marco, text="Futbol", variable=opcion, value=2, bg="lightblue", font=("Arial", 12, "bold")).pack(anchor="w")
tk.Radiobutton(marco, text="Voleybol", variable=opcion, value=3, bg="lightblue", font=("Arial", 12, "bold")).pack(anchor="w")
tk.Radiobutton(marco, text="Baloncesto", variable=opcion, value=4, bg="lightblue", font=("Arial", 12, "bold")).pack(anchor="w")

#Marcos de Botones
marco1 = tk.Frame(ventana, bg="lightblue", padx=10, pady=10)
marco1.pack(pady=10)

#Botón para guardar encuesta
guardar = tk.Button(marco1, text="Guardar", comman=guardar, font=("Arial", 12, "bold"),fg="white", bg="black",padx=10, pady=5)
#guardar.pack(pady=5)
guardar.grid(row=0, column=0, padx=5, pady=5)

#Botón para graficar
grafico = tk.Button(marco1, text="Graficar", comman=graficar, font=("Arial", 12, "bold"),fg="white", bg="red",padx=10, pady=5)
#grafico.pack(pady=5)
grafico.grid(row=0, column=1, padx=5, pady=5)

salir = tk.Button(ventana, text="Salir", comman=salir, font=("Arial", 12, "bold"),fg="black", bg="lightgreen",padx=10, pady=5)
salir.pack(padx=5, pady=5)

inactivos()



ventana.mainloop()

