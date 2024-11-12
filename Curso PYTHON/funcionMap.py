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
    Empleado("Pedro", "Programador backend", 40000),
    Empleado("Sofía", "Desarrollador Frontend", 47000),
    Empleado("Elena", "Operario", 22000),
    Empleado("Carlos", "Administrador", 85000)
]

# agregandole un bono a cada empleado con un salario menor o igual a 40000
def bonoEmpleados(empleado):
    if empleado.sueldo <= 40000:
        empleado.sueldo = empleado.sueldo * 1.05
        return str(empleado) + " (CON BONO)\n"
    else:
        return str(empleado) + "\n"

agregandoBono=map(bonoEmpleados, listaEmpleado)

contador = 1
for i in agregandoBono:
    print("{}. {}".format(contador,i))
    contador += 1