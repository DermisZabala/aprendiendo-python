import math

def vali_edad():
    edad = int(input("Introduce tu edad porfavor: "))

    while edad<4 or edad>100:
        print("Por favor introduce una edad valida")

        edad = int(input("Introduce una edad valida: "))

    print(f"Tu tienes {edad} años")


def raizCu2():
    intento = 0
    print("Buscando la raiz cuadrada de un numero.")

    num = int(input("Introduce un numero positivo: "))

    while num<0:
        print("El numero es negativo, porfavor ingrese un numero positivo")

        if intento==4:
            print("Lo haz intentado muchas veces, lo siento")
            break

        num=int(input("Vuelva a ingresar un numero: "))
        
        if num<0:
            intento+=1
    
    if intento < 4:
        numero2 = math.sqrt(num)

        print(numero2)
    else:
        print("El programa ha concluido")

raizCu2()