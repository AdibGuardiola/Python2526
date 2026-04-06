import numpy as np   # módulo

# a = np.array([1,2,3])   # función
# print(a.sum())   # método



#1 Tabla con NumPy

nombres = ["Juan", "Ana"]
edad = [20, 17]

datos = np.array(list(zip(nombres, edad)))

print("Nombre - Edad")
for lista in datos:
    print(lista[0], "-", lista[1])

print()


# 2  Multiplicar elementos de un array

a = np.array([1, 2, 3])
print("Array multiplicado por 2:", a * 2)

print()


# 3 Calcular la media

a = np.array([1, 2, 3])
print("La media es:", np.mean(a))

print()


#4 Filtrar valores mayores que 15

a = np.array([10, 20, 30, 40, 50, 60])
print("Valores mayores a 15:", a[a > 15])

print()


#5 Crear tabla con NumPy

nombres = ["Carlos", "María"]
edades = [12, 15]

datos = np.column_stack((nombres, edades))

print("Nombres - Edades")
for fila in datos:
    print(fila[0], "-", fila[1])

print()


#6 Filtrar mayores de edad

edades = np.array([20, 17, 34, 22, 15, 38])

mayores = edades[edades >= 18]

print("Edades mayores o iguales a 18:", mayores)


#7 Filtro de alturas

import numpy as np

nombres = np.array(["Juan", "Ana", "Luis", "Marta", "Pedro", "Sofía"])
alturas = np.array([180, 165, 175, 160, 172, 168])

# Filtro (mayores de 170 cm)
filtro = alturas >= 170

nombres_altos = nombres[filtro]
alturas_altas = alturas[filtro]

print("Personas con altura >= 170 cm:")
for i in range(len(nombres_altos)):
    print(nombres_altos[i], "-", alturas_altas[i])
