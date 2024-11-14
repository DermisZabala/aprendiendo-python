# creando el decorador
def funcion_decoradora(funcion_parametro):
    # '*args' lo que hace es recibir cualquier cantidad de argumetos como en la llamada a las funciones 'suma y multiplicacion'
    # '*kwargs lo que hace es recibir cualquier cantidad de argumentos con clave-valor como en la llamada a la funcion 'potencia''
    def funcion_interna(*args, **kwargs):
        print("Se esta realizando un calculo:")

        funcion_parametro(*args, **kwargs)

        print("Ya finalizo el calculo\n")

    return funcion_interna # devolviendo la funcion interna

# agregandole el decorador a suma
@funcion_decoradora
def suma(num1, num2):
    print(f"{num1} x {num2} = {num1 + num2}")

# agregandole el decorador a multiplicacion
@funcion_decoradora
def multiplicacion(num1, num2):
    print(f"{num1} x {num2} = {num1 * num2}")

# agregandole el decorador a multiplicacion
@funcion_decoradora
def potencia(base, exponente):
    print(f"{base} ^ {exponente} = {base ** exponente}")    

suma(20, 22)
multiplicacion(4, 6)
potencia(base = 5, exponente = 3)