"""
EJERCICIO 3
Una empresa tiene N empleados, con 0 <=N <= 1000
Se recibe el sueldo de cada empleado
y se desea el total de nomina
Para una empresa sin empleados,
El total es 0"""

N_empleados = int(input("Ingrese el numero de empleados: "))
nomina = 0

for sueldo in range (N_empleados):
    sueldo = float(input("sueldo del empleado: "))
    nomina = nomina + sueldo
    print ("Nomina: ", nomina)


