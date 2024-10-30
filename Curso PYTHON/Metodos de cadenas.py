print("Validando correo electronico GMAIL")

#correo = input("Ingrese su direccion de correo: ")
correo = "hamlzaba@gmail.com"

pospunto=correo.find('@') + 6

if correo.count('@') != 1:
    print("El correo es incorrecto")

elif correo[0] == '@' or correo[-1] == '@':
    print("El correo es incorrecto")

elif correo[0] == '.' or correo[-1] == '.':
    print("El correo es incorrecto")

elif correo[pospunto] != '.':
    print("El correo es incorrecto")

elif correo[-3] != 'c' and correo[-2] != 'o' and correo[-1] != 'm':
    print("El correo es incorrecto")

for i in correo:
    if i == ' ':
        print("El correo es incorrecto")
        break
else:
    print("El correo es correcto")