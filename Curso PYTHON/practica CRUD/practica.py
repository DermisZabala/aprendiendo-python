from tkinter import *
from tkinter import messagebox
import sqlite3

miConexion = None
miCursor = None

raiz = Tk()

nombre = StringVar()
apellido = StringVar()
contra = StringVar()
direccion = StringVar()
comentario = StringVar()

def limpiar():
    cajaDireccion.delete(0, END)
    cajaApellido.delete(0, END)
    cajaClave.delete(0, END)
    cajaComentario.delete(0, END)
    cajaNombreUsuario.delete(0, END)

def conexion():
    global miConexion, miCursor
    try:
        miConexion = sqlite3.connect("BaseDeDatosProyecto")
        # creando tabla
        miCursor = miConexion.cursor()

        miCursor.execute("""
                        CREATE TABLE USUARIOS 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_usuario VARCHAR(15), 
                        clave VARCHAR(50), 
                        apellido VARCHAR(15),
                        direccion VARCHAR(50),
                        comentario VARCHAR(100))
                        """)
        messagebox.showinfo("Conexion exitosa", "La base de datos se ha creado correctamente") 
    except sqlite3.OperationalError:
        messagebox.showwarning("Aviso", "Ya la base de datos esta creada")  

def salir():
    valor = messagebox.askokcancel("Salir", "Desea salir de la app?")
    if valor == True:
        raiz.destroy()

def crud(tipo):
    global miCursor, miConexion
    if tipo == "crear":
        valor1 = cajaNombreUsuario.get()
        valor2 = cajaClave.get()
        valor3 = cajaApellido.get()
        valor4 = cajaDireccion.get()
        valor5 = cajaComentario.get()
        datos = (valor1, valor2, valor3, valor4, valor5)
        print(datos[0])
        
        try:
            miConexion = sqlite3.connect("BaseDeDatosProyecto")
            miCursor = miConexion.cursor()
            miCursor.execute("INSERT INTO USUARIOS (nombre_usuario, clave, apellido, direccion, comentario) VALUES (?, ?, ?, ?, ?)", datos)
            miConexion.commit()
            messagebox.showinfo("Éxito", "Datos ingresador correctamente")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"No se pudo insertar los datos: {e}")
        finally:
            miConexion.close()
            limpiar()
    if tipo == "ver":
        datos = cajaID.get()
        try:
            miConexion = sqlite3.connect("BaseDeDatosProyecto")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT nombre_usuario FROM USUARIOS WHERE ID=?", datos)
            valor1 = miCursor.fetchall()
            nombre.set(valor1)
            miCursor.execute("SELECT clave FROM USUARIOS WHERE ID=?", datos)
            valor2 = miCursor.fetchall()
            contra.set(valor2)
            miCursor.execute("SELECT apellido FROM USUARIOS WHERE ID=?", datos)
            valor3 = miCursor.fetchall()
            apellido.set(valor3)
            miCursor.execute("SELECT direccion FROM USUARIOS WHERE ID=?", datos)
            valor4 = miCursor.fetchall()
            direccion.set(valor4)
            miCursor.execute("SELECT comentario FROM USUARIOS WHERE ID=?", datos)
            valor5 = miCursor.fetchall()
            comentario.set(valor5)
            miConexion.commit()
        except:
            messagebox.showerror("Error", "Ha ocurrido un error al intentar ver registro")

        
        


    if tipo == "actualizar":
        messagebox.showinfo("hola", "actualizar")
    if tipo == "eliminar":
        messagebox.showinfo("hola", "eliminar")


# creacion del menu
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=400, height=400)

# agregando los elementos a la barraMenu
conectBD = Menu(barraMenu, tearoff=0)
limpiarPantalla = Menu(barraMenu, tearoff=0)
accionesCRUD = Menu(barraMenu, tearoff=0)
archivoAyuda = Menu(barraMenu, tearoff=0)

# agregandole nombre a al menu
barraMenu.add_cascade(label="BBDD", menu=conectBD)
# subElementos a conectBD
conectBD.add_command(label="Conectar DB", command=conexion)
conectBD.add_command(label="Salir", command=salir)

barraMenu.add_cascade(label="Borrar", menu=limpiarPantalla)
limpiarPantalla.add_command(label="Limpiar patalla", command=limpiar)


barraMenu.add_cascade(label="CRUD", menu=accionesCRUD)
# subElementos a 
accionesCRUD.add_command(label="Crear", command=lambda: crud("crear"))
accionesCRUD.add_command(label="Visualizar", command=lambda: crud("ver"))
accionesCRUD.add_command(label="Actualizar")
accionesCRUD.add_command(label="Eliminar")


barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


miFrame = Frame()
miFrame.pack()



# cajas id
cajaID = Entry(miFrame)
cajaID.grid(row=0, column=1, padx=10, pady=5)

textoid = Label(miFrame, text="ID:", font=("arial", 10))
textoid.grid(row=0, column=0, sticky="w", padx=10, pady=5)


# cajas nombre_usuario
cajaNombreUsuario = Entry(miFrame, textvariable=nombre)
cajaNombreUsuario.grid(row=1, column=1, padx=10, pady=5)

textoNombreUsuario = Label(miFrame, text="Nombre:", font=("arial", 10))
textoNombreUsuario.grid(row=1, column=0, sticky="w", padx=10, pady=5)

# cajas clave
cajaClave = Entry(miFrame, textvariable=contra)
cajaClave.grid(row=2, column=1, padx=10, pady=5)

textoClave = Label(miFrame, text="Contraseña:", font=("arial", 10))
textoClave.grid(row=2, column=0, sticky="w", padx=10, pady=5)

# cajas APELLIDO
cajaApellido = Entry(miFrame, textvariable=apellido)
cajaApellido.grid(row=3, column=1, padx=10, pady=5)

textoApellido = Label(miFrame, text="Apellido:", font=("arial", 10))
textoApellido.grid(row=3, column=0, sticky="w", padx=10, pady=5)

# cajas direccion
cajaDireccion = Entry(miFrame, textvariable=direccion)
cajaDireccion.grid(row=4, column=1, padx=10, pady=5)

textoDireccion = Label(miFrame, text="Direccion:", font=("arial", 10))
textoDireccion.grid(row=4, column=0, sticky="w", padx=10, pady=5)

# cajas comentario
cajaComentario = Entry(miFrame, textvariable=comentario)
cajaComentario.grid(row=5, column=1, padx=10, pady=5)

textoComentario = Label(miFrame, text="Comentario:", font=("arial", 10))
textoComentario.grid(row=5, column=0, sticky="w", padx=10, pady=5)

# boton crear
miBoton1 = Button(miFrame, text="CREAR", command=lambda: crud("crear"))
miBoton1.config(bg="#42D09E", width=14)
miBoton1.grid(row=6, column=0, padx=5, pady=7)

# boton ver
miBoton2 = Button(miFrame, text="VER", command=lambda: crud("ver"))
miBoton2.config(bg="#42D09E", width=14)
miBoton2.grid(row=6, column=1, padx=5, pady=7)

# boton actualizar
miBoton3 = Button(miFrame, text="ACTUALIZAR", command=lambda: crud("actualizar"))
miBoton3.config(bg="#42D09E", width=14)
miBoton3.grid(row=6, column=2, padx=5, pady=7)

# boton eliminar
miBoton4 = Button(miFrame, text="ELIMINAR", command=lambda: crud("eliminar"))
miBoton4.config(bg="#42D09E", width=14)
miBoton4.grid(row=6, column=3, padx=15, pady=7)

raiz.mainloop()