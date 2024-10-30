validar = False

correo = input("Ingresa un correo electronico: ")

contador = 0

long_correo = len(correo)

pos_arroba = correo.find('@')

pos_punto = correo.find('.')

letra = '.'

posiciones = []

#p=0

for i in range(len(correo)):
    if correo[i] == letra:
        posiciones.append(i)
        #p=p+1

for i in correo:

    if i == "@" and correo[0] != "@":    
        contador = contador + 1

    if i == "." and pos_punto != 0 and correo[-1] != ".":
        validar=True


#try:
p = 0
for i in posiciones:
    if (posiciones[p]+1 == pos_arroba or 
        posiciones[p]-1 == pos_arroba):
        validar = False
    p = p+1
#except Exception:
#print("No hay puntos/o solo hay un punto")

if contador == 1 and validar == True:
    print("El correo es correcto")
else:
    print("El correo es incorrecto")


print(posiciones)
print(pos_arroba)