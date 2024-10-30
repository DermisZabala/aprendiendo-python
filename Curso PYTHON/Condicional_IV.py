def validacionBeca():
    print("\nValidacion de becas.\n")
    edad=int(input("Ingrese su edad: "))

    if 15<=edad<=17 or edad==18:
        distancia = int(input("Ingrese la distancia a la que vive del centro en KM: "))
        numHerm = int(input("Ingresa tu numero de hermanos: "))
        salarioFamiliar = float(input("Ingrese el salario familiar: "))
    else:
        print("Usted no cumple con la edad para adquirir una beca")

    if edad==18:
        #Si una sola condicion no se cumple ignora el if y entra en el else
        if distancia >= 40 and numHerm >= 2 and salarioFamiliar <= 20000:
            print("Usted se ha ganado una beca")
        else:
            print("Usted no tiene derecho a beca")
    elif 15<=edad<=17:
    #En esta caso si el estudiante es menor de edad 
    #se le dara la beca si la familia no gana un sueldo anual de 2000 
    #osea si las demas no se cumplen pero y solo se cumple el sueldo
    #si se le dara la beca
        if distancia >= 40 and numHerm >= 2 or salarioFamiliar <= 20000:
            print("Usted se ha ganado una beca")
        else:
            print("Usted no tiene derecho a beca")



def eleccionCarrera():
    print("Eligiendo una carrera.")

    print("\nCarreras disponibles:\
           \n1. Licenciatura en matematicas\
           \n2. Ingenieria en sistemas y computacion\
           \n3. Inteligencia artificial")
    
    eleccion = input("\nIngrese el nombre de la carrera que desea elegir:\n")

    carreras = eleccion.upper()
    print()

    if carreras in ("LICENCIATURA EN MATEMATICAS", "INGENIERIA EN SISTEMAS Y COMPUTACION", "INTELIGENCIA ARTIFICIAL"):        
        print("HA ELEGIDO " + carreras + " FELICIDADES")
    else:
        print("La asignatura que ingreso no es validad")

eleccionCarrera()

validacionBeca()