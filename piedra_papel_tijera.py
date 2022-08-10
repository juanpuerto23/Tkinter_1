# Importo la libreria tkinter, con el alias tk
import tkinter as tk
from tkinter import Tk, Label, Button, messagebox
import random

# Lista de variables
lista = ["Piedra", "Papel", "Tijera"]

#---------------------------
# Funciones operaciones
# --------------------------
def tijeras():
    Elección = random.choice(lista)
    opcion = "Tijera"
    if opcion == "Tijera" and Elección == "Tijera":
        messagebox.showinfo("Juego de Piedra, Papel o Tijeras", "El bot eligió Tijera \nEmpate")
    if opcion == "Tijera" and Elección == "Piedra":
        messagebox.showinfo("Juego de Piedra, Papel o Tijeras", "El bot eligió Piedra \nPerdiste")
    if opcion == "Tijera" and Elección == "Papel":
        messagebox.showinfo("Juego de Piedra, Papel o Tijeras", "El bot eligió Papel \nGanaste")

def Piedra():
    opcion = "Piedra"
    Elección = random.choice(lista)
    if opcion == "Piedra" and Elección == "Tijera":
        messagebox.showinfo("Juego de Piedra, Papel o Tijeras", "El bot eligió Tijera \nGanaste")
    if opcion == "Piedra" and Elección == "Piedra":
        messagebox.showinfo("Juego de Piedra, Papel o Tijeras", "El bot eligió Piedra \nEmpate")
    if opcion == "Piedra" and Elección == "Papel":
        messagebox.showinfo("Juego de Piedra, Papel o Tijeras", "El bot eligió Papel \nPerdiste")

def Papel():
    opcion = "Papel"
    Elección = random.choice(lista)
    if opcion == "Papel" and Elección == "Tijera":
        messagebox.showinfo("Juego de Piedra, Papel o Tijeras", "El bot eligió Tijera \nPerdiste")
    if opcion == "Papel" and Elección == "Piedra":
        messagebox.showinfo("Juego de Piedra, Papel o Tijeras", "El bot eligió Piedra \nGanaste")
    if opcion == "Papel" and Elección == "Papel":
        messagebox.showinfo("Juego de Piedra, Papel o Tijeras", "El bot eligió Papel \nEmpate")

def salir():
    ventana_principal.destroy() 

# -----------------------------
# VENTANA PRINCIPAL
# -----------------------------

# creacion objeto Tk (ventana principal)
ventana_principal = Tk()

# Titulo ventana principal
ventana_principal.title("Piedra, Papel o Tijera")

# dimensiones de la ventana
ventana_principal.geometry("500x200")

# deshabilitar boton maximizar
ventana_principal.resizable(0,0)

# color de fondo ventana principal
ventana_principal.config(bg="green")

# -----------------------------
# FRAME ENTRADA DE DATOS
# -----------------------------
frame_entrada = tk.Frame(ventana_principal)
frame_entrada.config(background = "#64b446", width = "480", height = "240")

# Titulo    
etiqueta1 = tk.Label(text = "Eligue el que quieras")
etiqueta1.pack(side = tk.TOP, padx = 10, pady = 20)

# boton Tijeras
frame_operaciones = tk.Frame(ventana_principal)
frame_operaciones.config(bg="gray", width=480, height=120)
frame_operaciones.place(x=10,y=65)
boton_tijeras = tk.Button(frame_operaciones, text="Tijeras", command = tijeras)
boton_tijeras.place(x=220, y=30)

# boton Papel
boton_papel = tk.Button(frame_operaciones, text="Papel", command = Papel)
boton_papel.place(x=40, y=30)

# boton Piedra
boton_piedra = tk.Button(frame_operaciones, text="Piedra", command = Piedra)
boton_piedra.place(x=400, y=30)

# boton Salir
boton_piedra = tk.Button(frame_operaciones, text="Salir", command = salir)
boton_piedra.place(x=225, y=80)

# desplegar ventana principal y queda a la espera de eventos del usuario
ventana_principal.mainloop()


