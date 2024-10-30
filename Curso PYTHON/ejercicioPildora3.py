print("Calculando la media aritmetica de 3 numero")

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

def mediaArit(numero1, numero2, numero3):
    suma = numero1 + numero2 + numero3

    laMedia = suma / 3

    return laMedia

print("La media aritmetica de ", num1, num2 ,\
      " y ", num3, " es " ,mediaArit(num1, num2, num3))