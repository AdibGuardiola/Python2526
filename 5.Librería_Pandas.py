# ==========================================
# 0. IMPORTAR LIBRERÍA
# ==========================================

import pandas as pd


# ==========================================
# 1. FUNCIÓN BÁSICA (sin pandas)
# ==========================================

def saludar(nombre):
    return f"Hola {nombre}"

print(saludar("Alumno"))


# ==========================================
# 2. CREAR DATOS (listas)
# ==========================================

def crear_datos():
    nombres = ["Ana", "Luis", "Marta", "Pedro"]
    edades = [15, 18, 17, 20]
    notas = [6, 4, 8, 5]
    return nombres, edades, notas

nombres, edades, notas = crear_datos()


# ==========================================
# 3. CREAR DATAFRAME
# ==========================================

def crear_dataframe(nombres, edades, notas):
    df = pd.DataFrame({
        "Nombre": nombres,
        "Edad": edades,
        "Nota": notas
    })
    return df

df = crear_dataframe(nombres, edades, notas)
print("\nDataFrame inicial:")
print(df)


# ==========================================
# 4. FUNCIÓN CON CONDICIONAL (filtrar)
# ==========================================

def filtrar_aprobados(df):
    return df[df["Nota"] >= 5]

print("\nAprobados:")
print(filtrar_aprobados(df))


# ==========================================
# 5. FUNCIÓN CON BUCLE (recorrer datos)
# ==========================================

def mostrar_nombres(df):
    print("\nLista de nombres:")
    for nombre in df["Nombre"]:
        print(nombre)

mostrar_nombres(df)


# ==========================================
# 6. FUNCIÓN CON BUCLE + CONDICIONAL
# ==========================================

def clasificar_notas(df):
    
    categorias = []
    
    for nota in df["Nota"]:
        if nota >= 5:
            categorias.append("Aprobado")
        else:
            categorias.append("Suspenso")
    
    df["Estado"] = categorias
    return df

df = clasificar_notas(df)
print("\nDataFrame con estado:")
print(df)


# ==========================================
# 7. FUNCIÓN CON CÁLCULOS
# ==========================================

def nota_media(df):
    return df["Nota"].mean()

print("\nNota media:", nota_media(df))


# ==========================================
# 8. FUNCIÓN QUE CUENTA ELEMENTOS
# ==========================================

def contar_aprobados(df):
    
    contador = 0
    
    for nota in df["Nota"]:
        if nota >= 5:
            contador += 1
    
    return contador

print("\nNúmero de aprobados:", contar_aprobados(df))


# ==========================================
# 9. FUNCIÓN MÁS COMPLETA
# ==========================================

def analizar_datos(df):
    
    total = len(df)
    aprobados = len(df[df["Nota"] >= 5])
    suspensos = total - aprobados
    
    return total, aprobados, suspensos

total, aprobados, suspensos = analizar_datos(df)

print("\nResumen:")
print("Total:", total)
print("Aprobados:", aprobados)
print("Suspensos:", suspensos)


# ==========================================
# 10. FUNCIÓN EXTRA (ordenar datos)
# ==========================================

def ordenar_por_nota(df):
    return df.sort_values(by="Nota", ascending=False)

print("\nOrdenado por nota:")
print(ordenar_por_nota(df))