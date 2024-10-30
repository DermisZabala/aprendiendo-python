
intento = 1; print("hola")

print("Realizando una operacion\n")

def operaciones(opcion):    
    if opcion == 1:
        num1 = input("Ingrese el primero numero: ")
        num1 = int(num1)
        num2 = input("Ingrese el segundo numero:")
        num2 = int(num2)
        resultado = num1 + num2
        return f"{num1} + {num2} = {resultado}"
    elif opcion == 2:
        num1 = input("Ingrese el primero numero: ")
        num1 = int(num1)
        num2 = input("Ingrese el segundo numero:")
        num2 = int(num2)
        resultado = num1 * num2
        return f"{num1} x {num2} = {resultado}"
    elif opcion == 3:
        num1 = input("Ingrese el primero numero: ")
        num1 = int(num1)
        num2 = input("Ingrese el segundo numero: ")
        num2 = int(num2)
        if num2 != 0:            
            resultado = num1 / num2
            return f"{num1} / {num2} = {resultado}"
        else:
            print("No se puede dividir entre 0")    
    else:
        print("Haz ingresado un numero incorrecto")


while intento != 0:
    opcion = int(input("Selecione una opcion:\
               \n1. Suma\
               \n2. Multiplicacion\
               \n3. Division\n"))


    print(operaciones(opcion))

    intento = int(input("\nPresiona 0 si deseas.\
            \nEn caso de que quieras continuar presione otro numero\n"))