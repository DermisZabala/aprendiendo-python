#Utilizando intrucciones continue, pass y else:

def continuar():
    print("Contando los caracteres tiene un nombre\n")
    nombre = input("Introduce tu nombre: ")
    
    contador = 0
    
    for i in nombre:
        if i == " ":
            continue
        contador+=1
    
    print(f"El nombre tiene {contador} letras")

#continuar()


#Utilizando ELSE
def usandoElse():
    print("Verificando si un email tiene @\n")

    email = input("Introduce un email, porfavor: ")

    for i in email:
        
        if i == "@":
            arroba = True
            break
    else:
        arroba = False
    
    print(arroba)

usandoElse()

#Utilizando pass
class MiClase:
    pass


print("fin del programa")
