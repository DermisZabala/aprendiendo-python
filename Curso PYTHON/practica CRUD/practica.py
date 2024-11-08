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
    cajaID.delete(0, END)
    cajaDireccion.delete(0, END)
    cajaApellido.delete(0, END)
    cajaClave.delete(0, END)
    cajaComentario.delete(1.0, END)
    cajaNombreUsuario.delete(0, END)

def conexion():
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

def crear():
    valor1 = cajaNombreUsuario.get()
    valor2 = cajaClave.get()
    valor3 = cajaApellido.get()
    valor4 = cajaDireccion.get()
    valor5 = cajaComentario.get("1.0", END).strip()
    datos = (valor1, valor2, valor3, valor4, valor5)   

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
        

def ver():
    datosID = cajaID.get()
    try:
        miConexion = sqlite3.connect("BaseDeDatosProyecto")
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT nombre_usuario FROM USUARIOS WHERE ID=?", datosID)
        valor1 = miCursor.fetchall()
        nombre.set(valor1)
        miCursor.execute("SELECT clave FROM USUARIOS WHERE ID=?", datosID)
        valor2 = miCursor.fetchall()
        contra.set(valor2)
        miCursor.execute("SELECT apellido FROM USUARIOS WHERE ID=?", datosID)
        valor3 = miCursor.fetchall()
        apellido.set(valor3)
        miCursor.execute("SELECT direccion FROM USUARIOS WHERE ID=?", datosID)
        valor4 = miCursor.fetchall()
        direccion.set(valor4)
        miCursor.execute("SELECT comentario FROM USUARIOS WHERE ID=?", datosID)
        valor5 = miCursor.fetchall()
        cajaComentario.insert(END, valor5)
        miConexion.commit()
    except:
        messagebox.showerror("Error", "Ha ocurrido un error al intentar ver registro")
    finally:
        miConexion.close() 

def actualizar():    
    datosACID = cajaID.get()
    valorAC1 = cajaNombreUsuario.get()
    valorAC2 = cajaClave.get()
    valorAC3 = cajaApellido.get()
    valorAC4 = cajaDireccion.get()
    valorAC5 = cajaComentario.get("1.0", END).strip()

    try:
        miConexion = sqlite3.connect("BaseDeDatosProyecto")
        miCursor = miConexion.cursor()

        if valorAC1:
            miCursor.execute("UPDATE USUARIOS SET nombre_usuario = ? WHERE ID = ?", (valorAC1, datosACID))
        if valorAC2:
            miCursor.execute("UPDATE USUARIOS SET clave = ? WHERE ID = ?", (valorAC2, datosACID))
        if valorAC3:
            miCursor.execute("UPDATE USUARIOS SET apellido = ? WHERE ID = ?", (valorAC3, datosACID))
        if valorAC4:
            miCursor.execute("UPDATE USUARIOS SET direccion = ? WHERE ID = ?", (valorAC4, datosACID))
        if valorAC5:
            miCursor.execute("UPDATE USUARIOS SET comentario = ? WHERE ID = ?", (valorAC5, datosACID))
        miConexion.commit()

    except:
        messagebox.showerror("Error","Error al momento de actualizar los datos")
    finally:
        miConexion.close()
        limpiar()

def eliminar():
    regis = cajaID.get()
    try:        
        miConexion = sqlite3.connect("BaseDeDatosProyecto")
        miCursor = miConexion.cursor()
        miCursor.execute("DELETE FROM USUARIOS WHERE ID = ?", regis)
        miConexion.commit()
        messagebox.showinfo("Exito", "Registro eliminado correctamente")
    except:
        messagebox.showerror("Error", "No se ha podido eliminar ningun registro")
    finally:
        miConexion.close()
        limpiar()


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
accionesCRUD.add_command(label="Crear", command=crear)
accionesCRUD.add_command(label="Visualizar", command=ver)
accionesCRUD.add_command(label="Actualizar", command=actualizar)
accionesCRUD.add_command(label="Eliminar", command=eliminar)


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
cajaClave.config(show="•")

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

# texto comentario
comentario=Label(miFrame, text="Comentario:", font=("arial", 13), bg="#9F74D6")
comentario.grid(row=5, column=0, sticky="w", padx=10, pady=5)
# caja comentario
cajaComentario = Text(miFrame, width=18, height=9)
cajaComentario.grid(row=5, column=1, padx=10, pady=5)
# barra de scroll para la caja comentario
miScroll = Scrollbar(miFrame, command=cajaComentario.yview)
miScroll.grid(row=5, column=2, sticky="nswe")
# desplazamiento de la barra
cajaComentario.config(yscrollcommand=miScroll.set)



# boton crear
miBoton1 = Button(miFrame, text="CREAR", command=crear)
miBoton1.config(bg="#42D09E", width=14)
miBoton1.grid(row=6, column=0, padx=5, pady=7)

# boton ver
miBoton2 = Button(miFrame, text="VER", command=ver)
miBoton2.config(bg="#42D09E", width=14)
miBoton2.grid(row=6, column=1, padx=5, pady=7)

# boton actualizar
miBoton3 = Button(miFrame, text="ACTUALIZAR", command=actualizar)
miBoton3.config(bg="#42D09E", width=14)
miBoton3.grid(row=6, column=2, padx=5, pady=7)

# boton eliminar
miBoton4 = Button(miFrame, text="ELIMINAR", command=eliminar)
miBoton4.config(bg="#42D09E", width=14)
miBoton4.grid(row=6, column=3, padx=15, pady=7)

raiz.mainloop()