#Creacion de la clase coche
class Coche():
    __ruedas = 4
    __movimiento = False

    #Creacion del constructor
    def __init__(self, peso, largo, ancho) -> None:
        self.__peso = peso
        self.__largo = largo
        self.__ancho = ancho
        
    #Metodo arrancar que comprueba si el coche esta parado o en movimiento
    def Arrancar(self, arrancando):
        self.__movimiento = arrancando
        if self.__movimiento == True:
            __chequeo = self.__chequeoInterno()

        if (self.__movimiento == True and __chequeo == True):
            return "El carro esta en movimiento"
        if (self.__movimiento == True and __chequeo == False):
            return "Se ha encontrado un fallo, el carro no puede arrancar"
        else:
            return "El carro esta parado"
    
    #Metodo estado que muestra las caracteristicas de los coches
    def Estado(self):
        return f"Peso del carro: {self.__peso} kg \nNumero de ruedas {self.__ruedas} \nAnchura del carro: {self.__ancho} cm \nLargo del carro: {self.__largo} cm"

    def __chequeoInterno(self):
        print("Se esta realizando un chequeo interno")

        self.__gasolina = "SI"
        self.__aceite = "SI"
        self.__puertas = "CERRADAS"

        if self.__gasolina == "SI" and self.__aceite == "SI" and self.__puertas == "CERRADAS":
            return True
        else:
            return False

    
print("------------Primer objeto------------")

#Creacion del objeto miCoche1
miCoche1 = Coche(1200, 321, 200)

#Llamada al metodo arrancar
print(miCoche1.Arrancar(True))
#Llamada al metodo estado
print(miCoche1.Estado())


print("------------Segundo objeto------------")

#Creacion del objeto miCoche2
miCoche2 = Coche(1700, 290, 199)

#Llamando a los metodos desde el segundo objeto
print(miCoche2.Arrancar(False))
print(miCoche2.Estado())