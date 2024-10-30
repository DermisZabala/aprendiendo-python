def operaciones(numero1, numero2):
    
    if opcion == "suma":    
        resultado = numero1 + numero2
    
    elif opcion == "resta":
        resultado = numero1 - numero2
    
    elif opcion == "division":        
        try: #Manejando la excepcion por si el usuario divide sobre 0
            resultado = numero1 / numero2
        
        except ZeroDivisionError:
            print("No se puede dividir sobre 0")

    elif opcion == "multiplicacion":
        resultado = numero1 * numero2
    
    else:
        print("La opcion que ingreso no existe")
    
    return resultado

try: #Capturando excepcion por si el usuario ingresa letras
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    op = input("Elija la operacion que desea realizar (suma, resta, division o multiplicacion):\n")

except ValueError:    
    print("Lo siento has ingresado letras")

try: #Manejando la excepcion por si las variables estan vacias o la funcion no llega a devolver un resultado
    opcion = op.lower()
    print(operaciones(num1, num2))
    
except NameError:
    print("El programa continua...")

