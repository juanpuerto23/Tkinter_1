from tkinter import Tk, Canvas, Scale, Frame, BOTH, Button
import tkinter as tk

BASE = 500
ALTURA = 500
RADIO = 60


ventana_principal = Tk()
ventana_principal.title("Molino")
ventana_principal.resizable(False, False)
ventana_principal.config(bg = "green")

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg = "white", width = 480, height = 400)
frame_graficacion.pack(fill=BOTH, padx = 10, pady = 10)

C = Canvas(frame_graficacion, width = BASE, height = ALTURA)
C.place(x = 10, y = 10)

triangulo = C.create_polygon(100, ALTURA - 25, (BASE / 2) - 50, 300, (BASE / 2) + 50, ALTURA - 15, fill = "blue", outline = "black")
circulo1 = C.create_arc((BASE / 2) - RADIO - 43, (ALTURA / 2) - RADIO + 40, (BASE / 2) + RADIO - 43, (ALTURA / 2) + RADIO + 40, start=0, extent=60, fill="blue", outline="")
circulo2 = C.create_arc((ALTURA / 2) - RADIO - 43, (BASE / 2) - RADIO + 40, (ALTURA / 2) + RADIO - 43, (BASE / 2) + RADIO + 40, start=0, extent=60, fill="blue", outline="")

boton= Button(text="Girar", padx=10,  fg="white", bg="blue")
boton.pack(side="left", padx=10, pady=10)

ventana_principal.mainloop()