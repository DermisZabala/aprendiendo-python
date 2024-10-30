print("Evaluando cual numero es mas alto\n")

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))


def DevuelveMax(numero1, numero2):

    if numero1 > numero2:
        return "El numero mas alto es: ", numero1
    elif numero2>numero1:
        return "El numero mas alto es: ", numero2
    else:
        return "Los numeros son iguales"

print(DevuelveMax(num1, num2))