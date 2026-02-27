# ===== TIPOS DE VARIABLES EN PYTHON =====


# ===== VARIABLES Y TIPOS BASICOS =====

#1 parte

# Entero
edad = 35
print("Edad:", edad)

# Decimal
altura = 1.75
print("Altura:", altura)

# Texto
nombre = "Adib"
print("Nombre:", nombre)

# Booleano
es_trader = True
print("Es trader:", es_trader)

#2 parte

print(type(edad))
print(type(altura))
print(type(nombre))
print(type(es_trader))

#3 parte

# Lista
pares = ["EURUSD", "USDCHF", "EURCHF"]
print(pares)
print(pares[0])  # EURUSD
print(pares[1])  # USDCHF

# Tupla
coordenadas = (10, 20)

# Diccionario
persona = {"nombre": "Adib", "edad": 35}

# Set
numeros = {1, 2, 3, 3}

#https://www.w3schools.com/python/python_datatypes.asp
#python -m http.server 8000