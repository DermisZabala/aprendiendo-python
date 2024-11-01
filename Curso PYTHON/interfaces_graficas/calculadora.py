from tkinter import *

raiz = Tk()

operacion = ""
signo = ""
numerosPantalla = StringVar()
resultado = 0

miFrame=Frame(raiz, width=500, height=500)
miFrame.config(bg="#42D09E")
miFrame.pack()

caja = Entry(miFrame, textvariable=numerosPantalla, width=23)
caja.grid(row=0, column=0, columnspan=3)

def botonPulsado(num):
    global operacion

    if num == "." and "." in numerosPantalla.get():
        return

    if operacion != "":
        numerosPantalla.set(num)
        operacion=""
    else:
        numerosPantalla.set(numerosPantalla.get() + num)

def suma(num):
    global operacion, resultado, signo

    resultado = int(numerosPantalla.get())
    operacion = "suma"
    numerosPantalla.set("")

    signo = "+"

def resta(num):
    global operacion, resultado, signo
    
    resultado = int(numerosPantalla.get())
    operacion = "resta"
    numerosPantalla.set("")

    signo = "-"

def multiplicacion(num):
    global operacion, resultado, signo
    
    resultado = int(numerosPantalla.get())
    operacion = "multiplicacion"
    numerosPantalla.set("")

    signo = "x"

def division(num):
    global operacion, resultado, signo
    
    resultado = int(numerosPantalla.get())
    operacion = "division"
    numerosPantalla.set("")

    signo = "/"


def elresultado():
    global operacion, resultado, signo

    if signo == "+":
        numerosPantalla.set(resultado + int(numerosPantalla.get()))
    elif signo == "-":
        numerosPantalla.set(resultado - int(numerosPantalla.get()))
    elif signo == "x":
        numerosPantalla.set(resultado * int(numerosPantalla.get()))
    elif signo == "/":
        if int(numerosPantalla.get()) != 0:
            numerosPantalla.set(resultado / int(numerosPantalla.get()))
        else:
            numerosPantalla.set("Error")

    resultado = 0
    operacion=""

def borrar():
    global resultado
    numerosPantalla.set(0)
    resultado=0

boton7 = Button(miFrame, text="7", command=lambda:botonPulsado("7"), width=5,height=3)
boton7.grid(row=1, column=0)


boton8 = Button(miFrame, text="8", command=lambda:botonPulsado("8"), width=5,height=3)
boton8.grid(row=1, column=1)


boton9 = Button(miFrame, text="9", command=lambda:botonPulsado("9"), width=5,height=3)
boton9.grid(row=1, column=2)


boton4 = Button(miFrame, text="4", command=lambda:botonPulsado("4"), width=5,height=3)
boton4.grid(row=2, column=0)

boton5 = Button(miFrame, text="5", command=lambda:botonPulsado("5"), width=5,height=3)
boton5.grid(row=2, column=1)


boton6 = Button(miFrame, text="6", command=lambda:botonPulsado("6"), width=5,height=3)
boton6.grid(row=2, column=2)


boton1 = Button(miFrame, text="1", command=lambda:botonPulsado("1"), width=5,height=3)
boton1.grid(row=3, column=0)


boton2 = Button(miFrame, text="2", command=lambda:botonPulsado("2"), width=5,height=3)
boton2.grid(row=3, column=1)

boton3 = Button(miFrame, text="3", command=lambda:botonPulsado("3"), width=5,height=3)
boton3.grid(row=3, column=2)

boton0 = Button(miFrame, text="0", command=lambda:botonPulsado("0"), width=5,height=3)
boton0.grid(row=4, column=0)

botonDiv = Button(miFrame, text="/", width=5,height=3, command=lambda:division(numerosPantalla.get()))
botonDiv.grid(row=4, column=1)

botonX = Button(miFrame, text="x", width=5,height=3, command=lambda:multiplicacion(numerosPantalla.get()))
botonX.grid(row=4, column=2)

botonRes = Button(miFrame, text="-", width=5,height=3, command=lambda:resta(numerosPantalla.get()))
botonRes.grid(row=5, column=0)

botonSum = Button(miFrame, text="+", width=5,height=3, command=lambda:suma(numerosPantalla.get()))
botonSum.grid(row=5, column=1)

botonIgual = Button(miFrame, text="=", width=5, height=3, command=lambda:elresultado())
botonIgual.grid(row=5, column=2)

botonborrar = Button(miFrame, text="C", width=5,height=3, command=lambda:borrar())
botonborrar.grid(row=6, column=0)

botonborrar = Button(miFrame, text=".", width=5, height=3, command=lambda:botonPulsado("."))
botonborrar.grid(row=6, column=1 )

raiz.mainloop()