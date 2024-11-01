from tkinter import *
from tkinter import filedialog

raiz = Tk()

def abreFichero():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros de texto","*.txt"), ("Ficheros pdf", "*.pdf"), ("Todos los archivo", "*.*")))

    print(fichero)

Button(raiz, text="Abrir fichero", command= abreFichero).pack()



raiz.mainloop()