#Creando tupla
miTupla=("Hamel", "Alex", "Eithan", 3, "Eithan")

#Valores que se repiten en la tupla
print("Solo hay ", miTupla.count(miTupla[2]), " elemento llamando: ", miTupla[2], " en la tupla")

#En que posicion se encuentra un valor
print("El elemento",miTupla[1],"se encuentra en la posicion",miTupla.index("Alex"))

#Cantidad de elementos que tiene la Tupla

print(len(miTupla))

#Pasa la tupla a una lista

miLista = list(miTupla)

#Imprimiento la lista
print(miLista)