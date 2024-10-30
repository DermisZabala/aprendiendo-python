#Creacion de la clase coche
class Coche():
    #Creacion del constructor
    def __init__(self, peso, largo, ancho) -> None:
        self.__peso = peso
        self.__ruedas = 4
        self.__largo = largo
        self.__ancho = ancho
        self.__movimiento = False

    #Metodo arrancar que comprueba si el coche esta parado o en movimiento
    def Arrancar(self, arrancando):
        self.__movimiento = arrancando
        if self.__movimiento == True:
            return "El carro esta en movimiento"
        else:
            return "El carro esta parado"
    
    #Metodo estado que muestra las caracteristicas de los coches
    def Estado(self):
        return f"Peso del carro: {self.__peso} kg \nNumero de ruedas {self.__ruedas} \nAnchura del carro: {self.__ancho} cm \nLargo del carro: {self.__largo} cm"
    
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


