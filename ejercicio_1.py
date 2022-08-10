from tkinter import Tk, Label

# Crea una ventana llamada root, de la clase TK. Se crea un objeto de la clase Tk
root = Tk()

# Definimos el tamaño de la ventana
root.geometry("500x500")

root.resizable(True, False)

root.minsize(50, 50)
root.maxsize(500, 500)

# Crear y agregar etiqueta a ventana
etiqueta = Label(text="\nUIS SOCORRO\n")
etiqueta.pack()

# Muestra la ventana y entra en un bucle infinito para la atención de eventos
root.mainloop()