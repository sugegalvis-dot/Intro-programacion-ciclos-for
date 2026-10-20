"""
Ejemplo:
Un profesor necesita crear un programa que le ayude a calcular el promedio de nitas de un salon de clases.
El ingresa el nombre y el valor de la nota final de cada estudiantes al final necesita saber cual es el mejor estudiante
y el promedio de todo el curso.
"""
cantidad_est = int(input("cantidad de estudiantes? "))

mejor_est =""
nota_mayor = 0.0
suma = 0.0
promedio = 0.0 

for veces in range (1, cantidad_est+1):
    print ("Estudiante #", veces)
    nombre = input("Nombre? ")
    nota = float (input("Nota? "))

    suma = suma + nota #<- Acumuladores

if nota > nota_mayor: #Encontrar estudiante con mayor nota
    nota_mayor = nota
    mejor_est = nombre 

promedio= suma / cantidad_est

print ("El promedio del curso es: ", promedio)
print ("El mejor estudiante es: ", mejor_est, "con nota de: ", nota_mayor)

