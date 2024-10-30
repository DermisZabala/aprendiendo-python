
def genera_numeros(h):
    num = 1
    while num < h:
        if num%2 == 0:
            yield(num)
        num = num + 1


numeros_generados = genera_numeros(20)

print("Primer elemento ", next(numeros_generados))

print("El programa continua...")

print("Segundo elemento ", next(numeros_generados))

print("El programa continua...")

print("Tercer elemento ", next(numeros_generados))