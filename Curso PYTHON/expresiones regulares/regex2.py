import re

lista_nombres = [
    "Hamel Zabala",
    "José martínez",
    "ana María Lopez",
    "María Fernanda Pérez",
    "Juan Pablo García",
    "Sofia Gomez",
    "Carlos Alvarez",
    "José Martinez",
    "Luis Hernández",
    "Ana Maria Lopez",
    "Raul Sanchez",
    "Lucía Ortega",
    "Raúl Sánchez",
    "Sofia Gómez",
    "Carlos Álvarez"
]

print("\nImprimiendo los elementos que empiecen por Ana")
for elemento in lista_nombres:
    if re.findall('^[aA]na', elemento):
        print(elemento)

print("\nImprimiendo los elementos que terminen por Martinez")
for elemento in lista_nombres:
    if re.findall('[Mm]art[ií]nez$', elemento):
        print(elemento)

print("\nImprimiendo los elementos que empiezan de la A a la G")
for elemento in lista_nombres:
    if re.findall('[A-B]', elemento):
        print(elemento)

