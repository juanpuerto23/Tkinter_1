# importo la libreria tkinter, con el alias ytk
import tkinter as tk

# creación objeto Tk (ventana principal)
ventana_principal = tk.Tk()

# Titulo ventana principal
ventana_principal.title("Bandera de Suiza")

# Dimensiones de la ventana
ventana_principal.geometry("500x500")

# Deshabilitar boton mazimizar
ventana_principal.resizable(0, 0)

# Color de fondo ventana principal
ventana_principal.config(bg = "red")

# Rectangulo vertical
frame_entrada = tk.Frame(ventana_principal)
frame_entrada.config(bg = "white", width = 100, height = 300)
frame_entrada.place(x = 200, y = 100)

#Rectangulo horizontal
frame_entrada = tk.Frame(ventana_principal)
frame_entrada.config(bg = "white", width = 300, height = 100)
frame_entrada.place(x = 100, y = 200)


# Desplegar ventana principal y queda a la espera de eventos del usuario
ventana_principal.mainloop()
