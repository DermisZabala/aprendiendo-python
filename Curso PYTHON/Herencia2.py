class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia
    
    def datos(self):
        print(f"Nombre: {self.nombre} \nEdad: {self.edad} \nLugar de residencia: {self.lugar_residencia}")

class Empleado(Persona):
    def __init__(self, id, salario, nombreEmpleado, edadEmpleado, lugar_residenciaEmpleado):
        super().__init__(nombreEmpleado, edadEmpleado, lugar_residenciaEmpleado)
        self.id = id
        self.salario = salario

    def datos(self):
        super().datos()
        print(f"Id: {self.id} \nSalario: {self.salario}")
    
miEmpleado = Empleado(10, 10220, "Hamel zabala", 19, "San Cristobal")
    
miEmpleado.datos()
