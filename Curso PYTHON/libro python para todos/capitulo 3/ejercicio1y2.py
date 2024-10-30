#Ejercicio 1: Reescribe el programa del cálculo del salario para darle al empleado
#1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.


print("Calculando el salario bruto")

try:
    horas = float(input("Ingrese las horas trabajadas:\n"))
    tarifa = float(input("Ingrese la tarifa:\n"))

    if horas > 40:
        horas_extra = horas - 40
        salarioB = (40 * tarifa) + (horas_extra * tarifa * 1.5)
    else:
        salarioB = horas * tarifa
    
    print("Salario bruto:" + str(salarioB))

except:
    print("Solo se aceptan valores numericos!!")

