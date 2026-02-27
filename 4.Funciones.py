# ==========================================
# CLASE — API REAL WORLD BANK (ROBUSTA)
# ==========================================

import requests

# ------------------------------------------
# 1️⃣ CONSTANTE (URL API)
# ------------------------------------------
API_URL = "https://api.worldbank.org/v2/country/{}/indicator/NY.GDP.MKTP.CD?format=json"

# ------------------------------------------
# 2️⃣ VARIABLE GLOBAL
# ------------------------------------------
paises = ["ESP", "USA", "CHN", "DEU"]
contador_global = 0


# ------------------------------------------
# 3️⃣ FUNCION BASICA
# ------------------------------------------
def saludo():
    print("Inicio script API")


# ------------------------------------------
# 4️⃣ FUNCION CON RETORNO
# ------------------------------------------
def obtener_gdp(country):
    url = API_URL.format(country)

    try:
        response = requests.get(url, timeout=5)
        data = response.json()
    except:
        print(f"{country}: error de conexion")
        return None

    if not isinstance(data, list) or len(data) < 2:
        return None

    for item in data[1]:
        if item["value"] is not None:
            return item["value"]

    return None


# ------------------------------------------
# 5️⃣ FUNCION MULTIPLES PARAMETROS
# ------------------------------------------
def mostrar_pib(country, gdp):
    print(f"{country} tiene PIB {gdp:.2f} USD")


# ------------------------------------------
# 6️⃣ PARAMETROS POR DEFECTO
# ------------------------------------------
def mensaje_error(country="Pais"):
    print(f"{country}: dato no disponible")


# ------------------------------------------
# 7️⃣ *ARGS
# ------------------------------------------
def suma_valores(*args):
    return sum(args)


# ------------------------------------------
# 8️⃣ **KWARGS
# ------------------------------------------
def mostrar_info(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


# ------------------------------------------
# 9️⃣ FUNCION LAMBDA
# ------------------------------------------
doble = lambda x: x * 2


# ------------------------------------------
# 🔟 FUNCION CON ANOTACIONES
# ------------------------------------------
def convertir_float(valor: float) -> float:
    return float(valor)


# ------------------------------------------
# 1️⃣1️⃣ FUNCION GLOBAL
# ------------------------------------------
def aumentar_contador():
    global contador_global
    contador_global += 1


# ------------------------------------------
# 1️⃣2️⃣ FUNCION ANIDADA
# ------------------------------------------
def contenedor():
    def interna():
        print("Funcion interna")
    interna()


# ------------------------------------------
# 1️⃣3️⃣ DECORADOR
# ------------------------------------------
def decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes funcion")
        resultado = func(*args, **kwargs)
        print("Despues funcion")
        return resultado
    return wrapper


@decorador
def funcion_decorada():
    print("Funcion decorada ejecutada")


# ------------------------------------------
# 1️⃣4️⃣ FUNCION GENERADORA
# ------------------------------------------
def generador_paises(lista):
    for p in lista:
        yield p


# ==========================================
# PROCESAR DATOS API
# ==========================================
saludo()

resultados = []

for country in generador_paises(paises):

    aumentar_contador()

    gdp = obtener_gdp(country)

    if gdp is None:
        mensaje_error(country)
        continue

    gdp = convertir_float(gdp)
    mostrar_pib(country, gdp)

    resultados.append((country, gdp))


# ==========================================
# TIPOS COMPUESTOS
# ==========================================
if resultados:
    lista = [c for c, _ in resultados]
    diccionario = dict(resultados)
    set_paises = set(lista)
    tupla_ejemplo = resultados[0]

    print("Lista:", lista)
    print("Dict:", diccionario)
    print("Set:", set_paises)
    print("Tupla:", tupla_ejemplo)

print("Contador global:", contador_global)

# uso extra funciones
print("Suma args:", suma_valores(1,2,3))
mostrar_info(nombre="Adib", rol="Trader")
print("Lambda:", doble(5))
contenedor()
funcion_decorada()