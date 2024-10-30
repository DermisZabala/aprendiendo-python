print("Almacenando datos del usuario\n")

datosUsuario = []

nombre = input("Ingrese su nombre: ")
direccion = input("Ingrese su direccion: ")
telefono = input("Ingrese su numero de telefono: ")

print("Datos usuario: \n")
print("  Nombre   \t  Direccion \t\t     Telefono")
datosUsuario.append(nombre)
datosUsuario.append(direccion)
datosUsuario.append(telefono)

print(datosUsuario)
