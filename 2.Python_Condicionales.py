# ==========================================
# CLASE 2 — CONDICIONALES EN PYTHON
# ==========================================

# ------------------------------------------
# 1️⃣ IF BASICO
# ------------------------------------------
edad = 18

if edad >= 18:
    print("Eres mayor de edad")


# ------------------------------------------
# 2️⃣ IF + ELSE
# ------------------------------------------
edad = 16

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")


# ------------------------------------------
# 3️⃣ IF + ELIF + ELSE
# ------------------------------------------
nota = 7

if nota >= 9:
    print("Sobresaliente")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")


# ------------------------------------------
# 4️⃣ OPERADORES DE COMPARACION
# ------------------------------------------
a = 10
b = 20

if a < b:
    print("a es menor que b")

if a == 10:
    print("a vale 10")

if a != b:
    print("a y b son distintos")


# ------------------------------------------
# 5️⃣ OPERADORES LOGICOS
# ------------------------------------------
edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puede conducir")

if edad >= 18 or tiene_carnet:
    print("Cumple al menos una condicion")

if not tiene_carnet:
    print("No tiene carnet")


# ------------------------------------------
# 6️⃣ EJEMPLO PRACTICO
# ------------------------------------------
precio = 120

if precio > 100:
    print("Producto caro")
else:
    print("Producto barato")


# ------------------------------------------
# 7️⃣ EJEMPLO CON TRADING
# ------------------------------------------
precio_eurusd = 1.08

if precio_eurusd > 1.10:
    print("Resistencia rota")
else:
    print("Aun en rango")


# ------------------------------------------
# 8️⃣ INPUT DEL USUARIO
# ------------------------------------------
edad_usuario = int(input("Introduce tu edad: "))

if edad_usuario >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")


# ------------------------------------------
# 9️⃣ EJERCICIO PARA ALUMNOS
# ------------------------------------------
# Pedir una nota y mostrar si aprueba

nota_usuario = int(input("Introduce tu nota: "))

if nota_usuario >= 5:
    print("Aprobado")
else:
    print("Suspenso")


# ------------------------------------------
# 🔟 EJERCICIO AVANZADO
# ------------------------------------------
# Sistema simple de decision de trading

precio = float(input("Introduce precio: "))

if precio > 1.10:
    print("Zona de venta")
elif precio < 1.05:
    print("Zona de compra")
else:
    print("Zona neutral")