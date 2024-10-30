#Crea un programa que pida números infinitamente. Los números introducidos deben 
#ser cada vez mayores El programa finalizará cuando se introduce un número menor que 
#el anterior.

def Ejercicio1():
    print("Introduciendo un numero mayor que el anterior")

    num = -9999999999999999

    while True:
        num1 = num
        num = int(input("Introduce un numero: "))    
        if num > num1:
            print(num)
        else:
            print("El " + str(num) + " no es mayor que el " + str(num1))
            break
    
    print("Has salido del programa")





#Ejercicio1()


#Crea un programa que pida números positivos indefinidamente. El programa termina 
#cuando se introduce un número negativo. Finalmente el programa muestras la suma de 
#todos los números introducidos

def Ejercicio2():
    print("Introduciendo solo numeros positivos")

    num=int(input("Introduce un numero: "))
    suma = 0 
    while num>0:
        suma = suma + num

        num=int(input("Introduce un numero: "))

    print(f"El total de los numeros que introduciste es: {suma}")

Ejercicio2()