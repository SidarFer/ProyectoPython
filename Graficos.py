

import matplotlib.pyplot as plt
import tkinter as tk


ventana=tk.Tk()
ventana.title("Vamos a graficar las ventas de sus Frutas")
ventana.geometry("450x400")

def graficar():
    frutas=['manzanas','bananas','piñas']
    ventas=[]

    #colores de las barras
    colores=['#ff9999','#66B2ff','#99FF99','#FFCC66']

    #Capturar datos del usuario
    fruta1 = float(campo_fruta1.get())
    fruta2 = float(campo_fruta2.get())
    fruta3 = float(campo_fruta3.get())
    ventas.append (fruta1)
    ventas.append (fruta2)
    ventas.append (fruta3)


    # crea graficos de barras
    plt.bar(frutas,ventas,color=colores)
    
    #Titulo Etiqueta
    plt.title("Vender frutas")
    plt.xlabel("Vender frutas")
    plt.ylabel("Vender frutas")

    # mostar el grafico
    plt.show()

def limpiar():
    campo_fruta1.delete(0, tk.END)
    campo_fruta2.delete(0, tk.END)
    campo_fruta3.delete(0, tk.END)
    campo_fruta1.focus()


#Campo donde el usuario puede escribir
tk.Label(ventana, text="Venta de Manzanas:", font=("Arial", 11, "bold")).pack(pady=(20,5))
campo_fruta1 = tk.Entry(ventana, font=("Arial", 12), width=30)
campo_fruta1.pack(pady=10)
campo_fruta1.focus()

tk.Label(ventana, text="Venta de Bananas:", font=("Arial", 11, "bold")).pack(pady=(20,5))
campo_fruta2 = tk.Entry(ventana, font=("Arial", 12), width=30)
campo_fruta2.pack(pady=10)

tk.Label(ventana, text="Venta de Piñas:", font=("Arial", 11, "bold")).pack(pady=(20,5))
campo_fruta3 = tk.Entry(ventana, font=("Arial", 12), width=30)
campo_fruta3.pack(pady=10)


#Botón Graficar
boton_graficar = tk.Button(ventana, text="Graficar", command=graficar, bg="orange")
boton_graficar.pack(pady=5)

#Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar, bg="yellow")
boton_limpiar.pack(pady=5)

ventana.mainloop()



