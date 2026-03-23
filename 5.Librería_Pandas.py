

import pandas as pd


# 1. Mostrar datos sin pandas

nombres = ["Juan", "Ana"]
edades = [20, 17]

for i in range(len(nombres)):
    print(nombres[i], "-", edades[i])
    
    

# 2. Mostrar datos con pandas


df = pd.DataFrame({
    "nombre": ["Juan", "Ana"],
    "edad": [20, 17]
})



#3. Filtrar  Edad con Pandas



df = pd.DataFrame({
    "edad": [20, 17]
})

print(len(df[df["edad"] >= 18]))


# 4. PEDIR DATOS AL USUARIO sin pandas


nombres = []
edades = []

print("Introduce alumnos (escribe 'salir' para terminar)\n")

while True:
    nombre = input("Nombre: ")
    
    if nombre.lower() == "salir":
        break
    
    edad = int(input("Edad: "))
    
    nombres.append(nombre)
    edades.append(edad)

#  FUERA del while
print("\nLista completa:")

for i in range(len(nombres)):
    print(nombres[i], "-", edades[i])
    
    
# 5. PEDIR DATOS AL USUARIO con pandas

import pandas as pd

nombres = []
edades = []

print("Introduce alumnos (escribe 'salir' para terminar)\n")

while True:
    nombre = input("Nombre: ")
    
    if nombre.lower() == "salir":
        break
    
    edad = int(input("Edad: "))
    
    nombres.append(nombre)
    edades.append(edad)

#  Crear DataFrame (aquí entra pandas)
df = pd.DataFrame({
    "nombre": nombres,
    "edad": edades
})

#  Mostrar datos en formato tabla
print("\nLista completa (pandas):")
print(df)

#  Generando tabla xls
df.to_excel("alumnos.xlsx", index=False)
print("\nArchivo 'alumnos.xlsx' creado correctamente")




#6 Filtrando desed XLS 

import pandas as pd

# Leer el Excel
df = pd.read_excel("alumnos.xlsx")

print("Datos completos:")
print(df)

# Filtrar mayores de edad
mayores = df[df["edad"] >= 18]

print("\nMayores de edad:")
print(mayores)
