# creando el decorador
def funcion_decoradora(funcion_parametro):
    def funcion_interna():
        print("Se realizando un calculo:")

        funcion_parametro()

        print("Finalizo el calculo\n")

    return funcion_interna # devolviendo la funcion interna

# agregandole el decorador a suma
@funcion_decoradora
def suma():
    print(f"7 + 4 = {7+4}")

# agregandole el decorador a multiplicacion
@funcion_decoradora
def multiplicacion():
    print(f"3 x 5 = {3 * 5}")
    

suma()
multiplicacion()