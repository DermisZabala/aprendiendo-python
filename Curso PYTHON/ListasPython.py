import array

#Jugando con las listas

#En python las listas pueden guardar diferentes tipos de datos#
numeros = [9, 0, 12, 2, 2.2, "2", False, True] 

print(numeros)

#----------------------------------------------------------------

#Agregando valores de un array a la lista numeros

miTupla = (0, 2, 13, 10, "hola") #Creacion del array

#Creacion de bucle for para agregar nuevos elementos a la lista

for i in miTupla:
    numeros.append(i) #Metodo append agrega valores a la lista 

print(numeros)

#----------------------------------------------------------------

#Duplicar los valores de una lista

print("\n",numeros) #Imprime 3 veces los valores que hay en la lista

#Imprimir los valores que desees de la lista

print("\n",numeros[0:3]) #imprime desde el primer al tercer elemento
print(numeros[-1]) #Imprime el ultimo elemento


#Eliminando valores de la lista

#Elimina la primera aparicion de un elemento
numeros.remove(9) #en este caso elimina el primer 9 en aparecer

numeros.pop() #elimina el elemento que esta en la posicion 1

# Validar si "hola" está en la lista antes de usar index
print("El primer 'hola' que aparezca en la lista se encuentra en la posición: ", numeros.index("hola"))

# Cuantas veces se repite un elemento
print("El elemento 'hola' se repite ", numeros.count("hola"), " veces")

# Imprimir la lista final
print(numeros)
