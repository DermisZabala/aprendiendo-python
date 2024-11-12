class Empleado:
    def __init__(self, nombre, puesto, sueldo):
        self.nombre = nombre
        self.puesto = puesto
        self.sueldo = sueldo
    
    def __str__(self):
        return "{} trabaja de {} su sueldo es de RD${}".format(self.nombre, self.puesto, self.sueldo)

listaEmpleado = [
    Empleado("Hamel", "Programador backend", 50000),
    Empleado("Miguel", "Operario", 20000),
    Empleado("Juan", "Administrador", 80000),
    Empleado("Luisa", "Analista de datos", 65000),
    Empleado("Mario", "Desarrollador Frontend", 45000),
    Empleado("Ana", "Operario", 21000),
    Empleado("Pedro", "Programador backend", 52000),
    Empleado("Sofía", "Desarrollador Frontend", 47000),
    Empleado("Elena", "Operario", 22000),
    Empleado("Carlos", "Administrador", 85000)
]

# filtrando los salarios menores a 50000
filtrandoS = lambda empleado : empleado.sueldo < 50000

filtrandoEmpleados = filter(filtrandoS, listaEmpleado)

o = 1
print("Empleados que tienen un sueldo menor de RD$50000")
for empleados in filtrandoEmpleados:
    print("{}. {}".format(o, empleados))
    o+=1

# filtrando los trabajadores con 'Operario'
filtrandoP = lambda empleado : empleado.puesto == "Operario"

filtrandoEmpleados = filter(filtrandoP, listaEmpleado)

print("\nEmpleados que tienen el puesto de operario")
o = 1
for i in filtrandoEmpleados:
    print("{}. {}".format(o, i))
    o+=1