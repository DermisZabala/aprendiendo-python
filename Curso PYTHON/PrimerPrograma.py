mensaje = "hola mundo"

num1 = 40
num2 = 40

suma = num1 + num2


print(num1, " + ", num2, " = ", suma)


print(mensaje)


print("""\nComparando que numero es mayor
      o si son iguales""")

print("\n")
numero1 = input("Ingrese el primer numero: ")
numero1 = int(numero1)

numero2 = input("Ingrese el segundo numero: ")
numero2 = int(numero2)

if (numero1>numero2):
    print("El numero 1 es mayor")
if(numero2>numero1):
    print("El numero 2 es mayor")
if numero2==numero1:
    print("Los numeros son iguales")