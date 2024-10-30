print("Evalua edad")

def evaluaEdad(edad):
    if edad<0:
        raise ValueError("Haz ingresado una edad negativa")
    elif edad < 13:
        print("Estas en la infancia")
    elif edad < 19:
        print("Estas en la adolescencia")
    elif edad < 36:
        print("Estas en la juventud")
    elif edad < 60:
        print("Estas en la adultez")
    elif edad <= 74:
        print("Estas en la adultez mayor")
    elif edad >= 75:
        print("Estas en la vejez")

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("Has ingresado un valor incorrecto. Vuelva a intentarlo!")

try:
    print(evaluaEdad(edad))

except ValueError as ExcepcionLanzada:
    print(ExcepcionLanzada)


