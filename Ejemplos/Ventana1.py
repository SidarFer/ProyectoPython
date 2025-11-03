
from tkinter import *

sifer=Tk()
ventana=Label(sifer,text="Esta es mi Primera Ventana en Python")
marco_principal=Frame()
ventana.pack()
marco_principal.pack()
marco_principal.config(width="400", height="200")
sifer.mainloop()
