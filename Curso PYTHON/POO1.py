class Coche():
    peso = 1500
    ruedas = 4
    largo = 320
    ancho = 210
    movimiento = False

    def Arrancar(self):
        self.Arrancar = True
    
    def Estado(self):
        if self.Arrancar == True:
            print("El carro esta en movimiento")
        else:
            print("El carro esta parado")
    
miCoche1 = Coche()

print(f"El coche tiene un largo de {miCoche1.largo} cm")
print(f"El coche tiene un ancho de {miCoche1.ancho} cm")
print(f"El coche tiene un peso de {miCoche1.peso} kg")
print(f"El coche tiene {miCoche1.ruedas} ruedas")

miCoche1.Arrancar()
miCoche1.Estado()