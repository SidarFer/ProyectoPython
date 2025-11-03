
import matplotlib.pyplot as plt
import tkinter as tk


ventana=tk.Tk()
ventana.title("Encuesta sobre Deportes")
ventana.geometry("450x400")

def limpiar():
    opcion_seleccionada.set(" ")
    


tk.Label(ventana, text="¿Cuántas personas participan en la Encuesta?:", font=("Arial", 11, "bold")).pack(pady=(20,5))
campo_fruta1 = tk.Entry(ventana, font=("Arial", 12), width=30)
campo_fruta1.pack(pady=10)
campo_fruta1.focus()

#Crear Frame
frame_opciones = tk.Frame(ventana, padx=10, pady=10)
frame_opciones.pack(pady=20)




#Crear y mostrar los botones de opción
opcion_seleccionada = tk.IntVar()
radio1 = tk.Radiobutton(frame_opciones, text="Beisbol", variable=opcion_seleccionada, value=1, justify="left")
radio2 = tk.Radiobutton(frame_opciones, text="Futbol", variable=opcion_seleccionada, value=2, justify="left")
radio3 = tk.Radiobutton(frame_opciones, text="Basquetbol", variable=opcion_seleccionada, value=3, justify="left")
radio4 = tk.Radiobutton(frame_opciones, text="Natación", variable=opcion_seleccionada, value=4, justify="left")

radio1.pack(anchor="w", pady=5)
radio2.pack(anchor="w", pady=5)
radio3.pack(anchor="w", pady=5)
radio4.pack(anchor="w", pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar, bg="yellow")
boton_limpiar.pack(pady=5)

ventana.mainloop()
