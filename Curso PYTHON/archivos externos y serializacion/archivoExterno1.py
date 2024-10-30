import io

#--------------------------CREANDO EL ARCHIVO--------------------------

def creando_escribiendo():
    #creando y manipulando el archivo externo
    archivo_texto = io.open("Archivo Externo 1.txt", "w")

    #añadiendo informacion al archivo
    archivo_texto.write("Hola mi nombre es Hamel\n") 

    archivo_texto.write("Soy Dominicano, tengo 20 años te amo bebe\n")


    #cerrando el archivo
    archivo_texto.close() 

#--------------------------LEYENDO EL ARCHIVO--------------------------
def leyendo_archivo():
    #cambiando la configuracion de 'write' a 'read'
    archivo_texto = io.open("Archivo Externo 1.txt", "r")

    #almacenando en la variable texto lo que hay en el archivo
    texto = archivo_texto.read()

    archivo_texto.close() #cerrando la conexion

    print(texto) #imprimiendo por consola lo que hay almacenado en el archivo

#-----------------------------AGREGANDO--------------------------------

def agregando_informacion():
    #añadiendo informacion en un archivo externo existente
    archivo_texto = io.open("Archivo Externo 1.txt", "a")

    #archivo_texto.write("como asi compai\n") #agregando mas informacion al archivo

    archivo_texto.close()

#-----------------------ALMACENANDO EN UNA LISTA-----------------------

def archivoEnLista():
    #almacenando cada una de las lineas del archivo en una lista
    archivo_texto = io.open("Archivo Externo 1.txt", "r")

    #creando la lista de cada una de las lineas del archivo
    lista = archivo_texto.readlines()

    #verificando que si es una lista
    print(type(lista))

    #cerrando la conexion
    archivo_texto.close()

    print("Lista:\n",lista) #mostrando la lista


def moviendoElPuntero():
    archivo = io.open("Archivo Externo 1.txt", "r+")

    """
    aqui lo que hago es poner el curso en la posicion 55 para modificar el texto
    de 'te amo' a 'y vivo en san cristobal'
    """
    #a = len(archivo.read()) - 11

    #archivo.seek(a)

    #archivo.write("y vivo en San Cristobal\n")

    """
    aqui pongo el curso en la posicion 0 para poner 'Presentacion:'
    """
    #archivo.seek(0)

    #archivo.write("Presentacion:\n")

    """
    aqui creo una lista para modificar el 
    texto que hay en el primer elemento osea el segundo elemento
    """
    lista2 = archivo.readlines()

    archivo.seek(0)

    lista2[1]="Hola mi nombre es Hamel\n"

    archivo.writelines(lista2)
    
    archivo.close()



#creando_escribiendo()
#leyendo_archivo()
#agregando_informacion()
#moviendoElPuntero()
#archivoEnLista()