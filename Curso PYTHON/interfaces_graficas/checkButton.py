from tkinter import *

raiz = Tk()

playa = IntVar()
montana = IntVar()
turismoRural = IntVar()

def opcionesViaje():
    opcionEscogida = ""
    if playa.get() == 1:
        opcionEscogida+=" Playa"
    if montana.get() == 1:
        opcionEscogida+=" Montaña"
    if turismoRural.get() == 1:
        opcionEscogida+=" Turismo Rural"

    textoFinal.config(text=opcionEscogida)

raiz.title("Ejemplo")

foto = PhotoImage(file="avion1.png")
Label(raiz, image=foto).pack()

frame = Frame(raiz)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()

Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesViaje).pack()

Checkbutton(frame, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()


raiz.mainloop()