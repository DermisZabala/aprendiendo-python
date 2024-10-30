class Coche():
    def desplazamiento(self):
        print("Me desplazo en 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo en 2 ruedas")

class Patana():
    def desplazamiento(self):
        print("Me desplazo en 6 ruedas")

def Desplazamientovehiculo(movimiento):
    movimiento.desplazamiento()

vehiculo = Coche()

Desplazamientovehiculo(vehiculo)