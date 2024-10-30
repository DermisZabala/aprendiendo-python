print("Accediendo a los elementos de la funcion")
def G_NombreCiudades(*ciudades):
    for i in ciudades:
        yield i

ciudadesCompletas = G_NombreCiudades("Bani", "Ocoa", "Azua")
print(next(ciudadesCompletas))
print(next(ciudadesCompletas))
print(next(ciudadesCompletas))

print("\nAccediendo a los sub-elementos de la funcion")
def G_ciudades(*ciudades):
    for i in ciudades:
        yield from i

ciudadesGeneradas = G_ciudades("Bani", "Ocoa", "Azua")
print("Primera")
print(next(ciudadesGeneradas))
print(next(ciudadesGeneradas))
print(next(ciudadesGeneradas))
print(next(ciudadesGeneradas))
print("Segunda")
print(next(ciudadesGeneradas))
print(next(ciudadesGeneradas))
print(next(ciudadesGeneradas))
print(next(ciudadesGeneradas))
print("Tercera")
print(next(ciudadesGeneradas))
print(next(ciudadesGeneradas))
print(next(ciudadesGeneradas))
print(next(ciudadesGeneradas))