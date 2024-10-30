import io

print("Realizar una presentacion")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nacionalidad = input("Ingrese su nacionalidad: ")

et = input("Si no se dedica a nada dele a tecla enter\n Escriba 'E' si estudia, Escriba 'T' si trabaja: ")

et = et.upper()



archivo = open(r"C:\Users\HP PROBOOK\OneDrive\Desktop\archivoExterno.txt", "w")

archivo.write("Presentacion:\n")
archivo.write("Mi nombre es {}, tengo {} años, soy {}\n".format(nombre, edad, nacionalidad))

if et == "E":
    carrera = input("Escriba su carrera: ")
    nivel =  int(input("Ingrese en numero cual es su nivel: "))
    archivo.write("Soy estudiante de {}, voy por el nivel {}".format(carrera, nivel))
elif et == "T":
    puesto = input("Diga cual es su puesto: ")
    anos = input("Cuantos años tiene en su puesto: ")
    archivo.write("Trabajo en {}, tengo {} años en el puesto".format())