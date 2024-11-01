from tkinter import *

raiz = Tk()

# Crear y configurar el Frame principal
miFrame = Frame(raiz, width=400, height=400)
miFrame.config(bg="#9F74D6")
miFrame.pack()

miNombre = StringVar()

# Crear y centrar el formulario dentro de miFrame
formulario = Frame(miFrame, bg="#9F74D6")
formulario.place(relx=0.5, rely=0.5, anchor="center")

# Título del formulario
Label(formulario, text="Formulario", font=("arial", 35), bg="#9F74D6").grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Etiqueta y caja de entrada para 'Nombre'
nombre = Label(formulario, text="Nombre:", font=("arial", 13), bg="#9F74D6")
nombre.grid(row=1, column=0, sticky="w", padx=10, pady=5)

cajanombre = Entry(formulario, textvariable=miNombre)
cajanombre.grid(row=1, column=1, padx=10, pady=5)

# Etiqueta y caja de entrada para 'apellido'
apellido = Label(formulario, text="Apellido:", font=("arial", 13), bg="#9F74D6")
apellido.grid(row=2, column=0, sticky="w", padx=10, pady=5)

cajaApellido = Entry(formulario)
cajaApellido.grid(row=2, column=1, padx=10, pady=5)

# Etiqueta y caja de entrada para 'Direccion'
direccion = Label(formulario, text="Direccion:", font=("arial", 13), bg="#9F74D6")
direccion.grid(row=3, column=0, sticky="w", padx=10, pady=5)

cajaDireccion = Entry(formulario)
cajaDireccion.grid(row=3, column=1, padx=10, pady=5)

# Etiqueta y caja de entrada para 'Contreseña'
contra = Label(formulario, text="Contreseña:", font=("arial", 13), bg="#9F74D6")
contra.grid(row=4, column=0, sticky="w", padx=10, pady=5)

cajaContra = Entry(formulario, show="*")
cajaContra.grid(row=4, column=1, padx=10, pady=5)


# caja de comentario
comentario=Label(formulario, text="Comentario:", font=("arial", 13), bg="#9F74D6")
comentario.grid(row=5, column=0, sticky="w", padx=10, pady=5)

cajaComentario = Text(formulario, width=18, height=9)
cajaComentario.grid(row=5, column=1, padx=10, pady=5)

# barra de scroll para la caja comentario
miScroll = Scrollbar(formulario, command=cajaComentario.yview)
miScroll.grid(row=5, column=2, sticky="nswe")

# desplazamiento de la barra
cajaComentario.config(yscrollcommand=miScroll.set)

def rCajaNombre():
    miNombre.set("Hamel")

# agregando un boton
miBoton = Button(formulario, text="Enviar!!", command=rCajaNombre)
miBoton.config(bg="#42D09E")
miBoton.grid(row=6, column=0, columnspan=2, padx=10, pady=7)

# Ejecutar el loop principal de la ventana
raiz.mainloop()
