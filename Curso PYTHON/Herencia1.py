#Creacion de la superclase Vehiculo
class Vehiculos():
    #Constructor para inicializar las variables
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.__en_marcha = False
        self.__acelerar = False
        self.__frenar = False

    #Creacion del metodo arrancar
    def arrancar(self):
        self.__en_marcha = True
    
    #Creacion del metodo acelerando
    def acelerando(self):
        self.__acelerar = True

    #Creacion del metodo frenar
    def frenando(self):
        self.__frenar = True
    
    #Metodo que indica el estado del vehiculo
    def estado(self):
        print(f"Marca: {self.__marca} \nModelo: {self.__modelo} \nArrancando: {self.__en_marcha} \nAcelerando: {self.__acelerar} \nFrenando: {self.__frenar}")

#creacion de la subclase 'Carro' que hereda de la superclase 'Vehiculo'
class Moto(Vehiculos):
    calibrando = ""
    def calibrar(self, calibra):
            
        if calibra == True:
            self.calibrando = "Usted esta calibrando"
        else:
            print("Usted anda en 2 ruedas")
        
    def estado(self):
        super().estado()
        print(self.calibrando)


miMoto1 = Moto("Suzuki", "AX-100")

miMoto1.calibrar(True)

miMoto1.estado()

class Patana(Vehiculos):
    def cargada(self, cargando):
        if cargando == True:
            print("La patana esta cargada")
        else:
            print("La patana esta vacia")

miPatana = Patana("Toyota", "Nose")
print("---------------------------")
miPatana.estado()
miPatana.cargada(False)

class Vehtro():
    def __init__(self):
        self.autonomia = 100

    def cargaEnergia(self):
        self.bateria = 60
        print("Carga de la bateria: " ,self.bateria, "%")

#SubClase quen 
class BicicletaElectrica(Vehiculos, Vehtro):
    pass

miBici = BicicletaElectrica("BMX", "NOSE")

print("-----------------------------------------------")
miBici.cargaEnergia()
miBici.estado()


