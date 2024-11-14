import re
import os

e = 0

lista_nombres = [
    "ana Zabala",
    "José martínez",
    "ana María Lopez",
    "María Fernanda Alvarez",
    "Juan Pablo García",
    "Sofia Gomez",
    "Carlos Alvarez",
    "José Martinez",
    "Luis Hernández",
    "Ana Maria Lopez",
    "ana Sanchez",
    "Lucía Ortega",
    "Raúl Lopez",
    "Sofia Gómez",
    "Ana Álvarez"
]

# utilizando la funcion match para buscar los elementos que empiecen por Ana ignorando las letras mayusculas y minusculas
for elemento in lista_nombres:
    if re.match("ana", elemento, re.IGNORECASE):       
        print(elemento)
        e+=1

print(f"Se han encontrado {e} Ana\n")

e=0
''' 
utilizando la funcion search para buscar los en cualquier 
parte del elemento el apellido Alvarez ignorando mayusculas y la tilde 
'''
for elemento in lista_nombres:
    if re.search("[ÁA]lvarez",elemento, re.IGNORECASE):
        print(elemento)
        e+=1

print(f"Se han encontrado {e} Álvarez")

os.system('cls')

# Lista de códigos con letras y números
lista_codigos = [
    "A123B456",
    "B789C012",
    "XYZ987",
    "AB123CD",
    "123ABC456",
    "X1Y2Z3",
    "LMN456OPQ",
    "AB12",
    "PQR345ST",
    "789XYZ",
    "CD123EFG",
    "987LMN654",
    "QR123",
    "STU456VWX",
    "456PQR789"
]

e = 0
print("Buscando los codigos que tengan el numero '456'")
for elemento in lista_codigos:
    if re.search("456", elemento):
        print(elemento)
        e+=1

if not e == 0:
    print("Se han encontrado {} codigos".format(e))
else:
    print("No se encontro ningun codigo con el numero '456'")

