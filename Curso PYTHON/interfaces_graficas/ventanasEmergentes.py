from tkinter import *
from tkinter import messagebox

raiz = Tk()

def acercaDe():
    #ventana de informacion
    messagebox.showinfo("Procesador de Hamel", "Precesador de textos version 2024")

def avisoLincencia():
    #ventana de aviso
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def ventanaSalir():
    #ventana para salir
    #valor = messagebox.askquestion("Salir", "Haga clic en 'si' para salir 'no' para cancelar")

    valor = messagebox.askokcancel("Salir", "Desea salir de la aplicacion?")

    if valor == True:
        raiz.destroy()

def ventanaCerrarDocumento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")

    if valor == False:
        raiz.destroy()


# creacion del menu
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=400, height=400)

# agregando los elementos a la barraMenu
archivoMenu = Menu(barraMenu, tearoff=0)
archivoEdicion = Menu(barraMenu, tearoff=0)
archivoHerramienta = Menu(barraMenu, tearoff=0)
archivoAyuda = Menu(barraMenu, tearoff=0)

# agregandole nombre a al menu
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramienta", menu=archivoHerramienta)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

# subElementos a archivoMenu
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
# separar los elementos cerrar y salir de los demas
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=ventanaCerrarDocumento)
archivoMenu.add_command(label="Salir", command=ventanaSalir)

# subElementos a archivoEdicion
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

#subElementos a archivoAyuda
archivoAyuda.add_command(label="Licencia", command=avisoLincencia)
archivoAyuda.add_command(label="Acerca de", command=acercaDe)


raiz.mainloop()