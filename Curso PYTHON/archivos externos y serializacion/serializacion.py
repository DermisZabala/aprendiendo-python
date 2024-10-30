from pickle import load, dump

archivo = open("Archivo Serializacion", "rb")

#dump(lista, archivo)

a = load(archivo)

print(a)