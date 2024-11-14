import re

cadena = "Hola mi nombre es Hamel. Ese nombre me lo puso mi mama"

buscar = "nombre"

print(re.findall(buscar, cadena))

print(f"'{buscar}' se ha encontrado {len(re.findall(buscar, cadena))} en la cadena")

# las veces que se repite nombre en la cadena y que posiciones se encuentran
repeticion = re.finditer(buscar, cadena)

for i in repeticion:
    print(i.span()) # devuelve una tupla que contiene (inicio, final) las posiciones de coincidencia