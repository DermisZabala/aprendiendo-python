#Ejercicio 2: Reescribe el programa del salario usando try y except, de modo que el
#programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando
#un mensaje y saliendo del programa. A continuación se muestran dos ejecuciones
#del programa:

print("Puntuacion calificacion")
calificacion = -1
try:
    calificacion = float(input("Ingrese su calificacion 0.0 y 1.0:\n"))
except:
    print("Error de calificacion")

if calificacion < 0 or calificacion > 1.0:
    print("Puntuacion Erronea")
elif calificacion >= 0.9:
    print("Sobresaliente")
elif calificacion >= 0.8:
    print("Notable")
elif calificacion >= 0.7:
    print("Bien")
elif calificacion >= 0.6:
    print("Suficiente")
elif calificacion < 0.5:
    print("Insuficiente")
