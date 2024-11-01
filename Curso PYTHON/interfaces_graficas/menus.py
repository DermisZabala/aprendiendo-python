from tkinter import *

raiz = Tk()

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
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

# subElementos a archivoEdicion
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

#subElementos a archivoAyuda
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de")


raiz.mainloop()