#Diccionario que almacena las notas de los estudiantes
almacenDeNotas = {}

cantidad = 0
clave = 0

def agregar():
    global clave
    
    cantidad = 0
    cantidadEst = int(input("Ingrese la cantidad de los estudiantes:\n"))
    
    while cantidadEst > cantidad:
        
        nombreEstu = input("Ingrese el nombre del estudiante: ")

        cF = int(input("Ingrese la calificacion del estudiante: "))
        
        clave+=1

        almacenDeNotas[clave] = {"Nombre: ",nombreEstu, "Calificacion: ",cF}

        cantidad+=1

def verCalificacion():
    print("CALIFICACION DE LOS ESTUDIANTES.")
    print("________________________________________________________")
    for i in almacenDeNotas:
        #Desempaquetando la el diccionario
        nombres, calificaciones = almacenDeNotas[i]

        if calificaciones > 69 and calificaciones <= 100:
            print("Clave ", i ,":",almacenDeNotas[i], " Aprobo")
                
        elif calificaciones < 70 and calificaciones >= 0:
            print("Clave ", i ,":",almacenDeNotas[i], " Reprobo")
                
        else:
            print("ERROR: Clave ", i ,":", almacenDeNotas[i], " la calificacion es erronea porfavor corrigela")
    print("________________________________________________________")


def corregirCal():
    print("________________________________________________________")
    print("ACTUALIZANDO REGISTRO.\n")
    print("________________________________________________________")
    clave=int(input("Ingrese la clave del estudiante: "))

    nombre = input("\nIngrese el nombre del estudiante: ")
    nuevaCF = int(input("Ingrese la nueva nota: "))
    almacenDeNotas[clave]= nombre, nuevaCF
    print("________________________________________________________")


def eliminarEstu():
    print("________________________________________________________")
    print("ELIMINANDO REGISTRO.")
    clave=int(input("Ingrese la clave del estudiante que desea eliminar: "))
    del almacenDeNotas[clave]
    print("________________________________________________________")



vueltas = False

while vueltas != True:
    print("________________________________________________________")
    op = input("Seleccione una opcion:\
          \n1. Para agregar una calificacion presione la tecla 'A'\
          \n2. Para ver Calificaciones presione la tecla 'V'.\
          \n3. Para Corregir Calificaciones presione la tecla 'C'.\
          \n4.Para Eliminar Calificaciones presione la tecla 'E'.\
          \nPresione cualquier otra letra para salir\n")
    print("________________________________________________________")
    op = op.upper()

    if op == "A":
        agregar()
    elif op == "V":
        verCalificacion()
    elif op == "C":
        corregirCal()
    elif op == "E":
        eliminarEstu()
    else:
        vueltas = True
        