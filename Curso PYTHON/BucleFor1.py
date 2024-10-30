print("Validacion de correo")

contador = 0
contadorPunto = 0

correo = ".hamel11@gmail.com"

arroba_pos = correo.index("@")
punto_pos = correo.rindex(".")

print(arroba_pos)
print(punto_pos)

# Recorrer cada carácter de la cadena y contar los símbolos relevantes


for i in correo:
    if i == "@":
        if arroba_pos > 5 and arroba_pos < 66:
                contador = contador + 1

    elif i == ".":
        if arroba_pos != 0 and i != len(correo) - 1:
            contadorPunto = contadorPunto + 1

# Verificar si hay exactamente un @ y al menos un punto
if contador == 1 and contadorPunto >= 1:
    print("El correo es válido")
else:
    print("El correo es incorrecto")

print(contador)
print(contadorPunto)

print(len(correo))