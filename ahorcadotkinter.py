
import tkinter as tk
from tkinter import messagebox
import random

# --- Palabras posibles ---
PALABRAS = ["SIDAR", "AHORCADO", "PYTHON", "JUEGO", "LEON", "NICARAGUA", "INATEC"]

# --- Configuración del juego ---
palabra = random.choice(PALABRAS)
letras_adivinadas = []
intentos_restantes = 6

# --- Crear ventana principal ---
ventana = tk.Tk()
ventana.title("Juego del Ahorcado")
ventana.geometry("400x550")
ventana.resizable(False, False)

# --- Funciones del juego ---
def actualizar_palabra():
    """Muestra las letras adivinadas y oculta las no descubiertas."""
    palabra_mostrada = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "
    lbl_palabra.config(text=palabra_mostrada.strip())

def comprobar_letra():
    """Verifica si la letra ingresada está en la palabra."""
    global intentos_restantes

    letra = entrada_letra.get().upper()
    entrada_letra.delete(0, tk.END)

    # Validación
    if not letra.isalpha() or len(letra) != 1:
        messagebox.showwarning("Advertencia", "Introduce una sola letra válida.")
        return

    if letra in letras_adivinadas:
        messagebox.showinfo("Aviso", "Ya adivinaste esa letra.")
        return

    letras_adivinadas.append(letra)

    if letra in palabra:
        actualizar_palabra()
        if all(l in letras_adivinadas for l in palabra):
            messagebox.showinfo("🎉 ¡Ganaste!", f"Adivinaste la palabra: {palabra}")
            reiniciar_juego()
    else:
        intentos_restantes -= 1
        lbl_intentos.config(text=f"Intentos restantes: {intentos_restantes}")
        dibujar_ahorcado()
        if intentos_restantes == 0:
            messagebox.showerror("💀 Fin del Juego", f"La palabra era: {palabra}")
            reiniciar_juego()

def reiniciar_juego():
    """Reinicia el juego con una nueva palabra."""
    global palabra, letras_adivinadas, intentos_restantes
    palabra = random.choice(PALABRAS)
    letras_adivinadas = []
    intentos_restantes = 6
    lbl_intentos.config(text=f"Intentos restantes: {intentos_restantes}")
    canvas.delete("all")
    actualizar_palabra()

def dibujar_ahorcado():
    """Dibuja el ahorcado según los intentos restantes."""
    if intentos_restantes == 5:
        canvas.create_line(20, 230, 180, 230, width=3)  # base
    elif intentos_restantes == 4:
        canvas.create_line(100, 230, 100, 50, width=3)  # poste
    elif intentos_restantes == 3:
        canvas.create_line(100, 50, 180, 50, width=3)   # barra superior
        canvas.create_line(180, 50, 180, 70, width=3)   # cuerda
    elif intentos_restantes == 2:
        canvas.create_oval(160, 70, 200, 110, width=2)  # cabeza
    elif intentos_restantes == 1:
        canvas.create_line(180, 110, 180, 170, width=2)  # cuerpo
        canvas.create_line(180, 130, 160, 150, width=2)  # brazo izq
        canvas.create_line(180, 130, 200, 150, width=2)  # brazo der
    elif intentos_restantes == 0:
        canvas.create_line(180, 170, 160, 200, width=2)  # pierna izq
        canvas.create_line(180, 170, 200, 200, width=2)  # pierna der

# --- Controles ---
lbl_titulo = tk.Label(ventana, text="JUEGO EL AHORCADO", font=("Arial", 16, "bold"))
lbl_titulo.pack(pady=10)

lbl_palabra = tk.Label(ventana, text="", font=("Consolas", 24))
lbl_palabra.pack(pady=20)

lbl_intentos = tk.Label(ventana, text=f"Intentos restantes: {intentos_restantes}", font=("Arial", 12))
lbl_intentos.pack()

entrada_letra = tk.Entry(ventana, font=("Arial", 14), width=5, justify="center")
entrada_letra.pack(pady=10)

btn_comprobar = tk.Button(ventana, text="Comprobar", font=("Arial", 12), command=comprobar_letra)
btn_comprobar.pack()

canvas = tk.Canvas(ventana, width=250, height=250, bg="lightblue")
canvas.pack(pady=10)

# Inicializar la palabra oculta
actualizar_palabra()

# --- Ejecutar el juego ---
ventana.mainloop()