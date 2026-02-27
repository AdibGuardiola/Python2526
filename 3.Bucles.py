# ==========================================
# TODOS LOS BUCLES EN PYTHON
# ==========================================

# ------------------------------------------
# 1️⃣ FOR CON LISTA
# ------------------------------------------
pares = ["EURUSD", "USDCHF", "GBPUSD"]

for par in pares:
    print("Lista:", par)


# ------------------------------------------
# 2️⃣ FOR CON RANGE
# ------------------------------------------
for i in range(3):
    print("Range:", i)


# ------------------------------------------
# 3️⃣ FOR CON DICCIONARIO (SOLO CLAVES)
# ------------------------------------------
gdp_data = {
    "Spain": 1.4,
    "USA": 25.0,
    "China": 18.0
}

for country in gdp_data:
    print("Clave:", country)


# ------------------------------------------
# 4️⃣ FOR CON DICCIONARIO (SOLO VALORES)
# ------------------------------------------
for gdp in gdp_data.values():
    print("Valor:", gdp)


# ------------------------------------------
# 5️⃣ FOR CON DICCIONARIO (CLAVE + VALOR)
# ------------------------------------------
for country, gdp in gdp_data.items():
    print("Clave y valor:", country, gdp)


# ------------------------------------------
# 6️⃣ FOR CON INDICE (enumerate)
# ------------------------------------------
for i, par in enumerate(pares):
    print("Indice:", i, "Valor:", par)


# ------------------------------------------
# 7️⃣ FOR ANIDADO
# ------------------------------------------
matriz = [[1,2], [3,4]]

for fila in matriz:
    for numero in fila:
        print("Anidado:", numero)


# ------------------------------------------
# 8️⃣ WHILE BASICO
# ------------------------------------------
i = 0
while i < 3:
    print("While:", i)
    i += 1


# ------------------------------------------
# 9️⃣ WHILE CON BREAK
# ------------------------------------------
i = 0
while True:
    print("While infinito:", i)
    i += 1
    if i == 3:
        break


# ------------------------------------------
# 🔟 FOR CON CONTINUE
# ------------------------------------------
for i in range(5):
    if i == 2:
        continue
    print("Continue:", i)


# ------------------------------------------
# 1️⃣1️⃣ FOR CON BREAK
# ------------------------------------------
for i in range(5):
    if i == 3:
        break
    print("Break:", i)


# ------------------------------------------
# 1️⃣2️⃣ FOR CON ZIP
# ------------------------------------------
paises = ["Spain", "USA", "China"]
gdp = [1.4, 25.0, 18.0]

for country, value in zip(paises, gdp):
    print("Zip:", country, value)


# ------------------------------------------
# 1️⃣3️⃣ FOR SOBRE STRING
# ------------------------------------------
for letra in "EURUSD":
    print("String:", letra)


# ------------------------------------------
# 1️⃣4️⃣ WHILE CON INPUT
# ------------------------------------------
contador = 0
while contador < 2:
    print("While input ejemplo")
    contador += 1


# ------------------------------------------
# 1️⃣5️⃣ LIST COMPREHENSION (BUCLE COMPACTO)
# ------------------------------------------
cuadrados = [x**2 for x in range(5)]
print("List comprehension:", cuadrados)