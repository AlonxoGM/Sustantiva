import tkinter as tk
from tkinter import messagebox
import random

opciones = [
    "Lista",
    "Tupla",
    "Diccionario"
]

def verificar_respuesta(respuesta):
    if respuesta == "Lista":  
        resultado = "¡Sí, efectivamente es!"
    else:
        resultado = "No, intenta de nuevo"
    messagebox.showinfo("Resultado", resultado)

def mostrar_pregunta():
    opciones_aleatorias = random.sample(opciones, 3)
    ventana_opciones = tk.Toplevel()
    ventana_opciones.title("Elige el tipo de lista")

    for opcion in opciones_aleatorias:
        boton_opcion = tk.Button(ventana_opciones, text=opcion, command=lambda o=opcion: verificar_respuesta(o))
        boton_opcion.pack()

ventana = tk.Tk()
ventana.title("Programa de Listas en Python")

boton_pregunta = tk.Button(ventana, text="Elije el tipo de lista", command=mostrar_pregunta)
boton_pregunta.pack()

ventana.mainloop()
