# ==========================================
# 0. IMPORTAR LIBRERÍA
# ==========================================

import streamlit as st


# ==========================================
# 1. FUNCIÓN BÁSICA
# ==========================================

def saludar(nombre):
    return f"Hola {nombre}"

st.write(saludar("Alumno"))


# ==========================================
# 2. INPUT DEL USUARIO
# ==========================================

nombre = st.text_input("Introduce tu nombre")

if nombre:
    st.write(saludar(nombre))


# ==========================================
# 3. CONDICIONAL
# ==========================================

edad = st.number_input("Introduce tu edad", min_value=0, max_value=100)

def es_mayor(edad):
    if edad >= 18:
        return "Eres mayor de edad"
    else:
        return "Eres menor de edad"

if edad:
    st.write(es_mayor(edad))


# ==========================================
# 4. BOTÓN
# ==========================================

if st.button("Mostrar mensaje"):
    st.write("Has pulsado el botón")


# ==========================================
# 5. BUCLE (mostrar lista)
# ==========================================

def mostrar_lista():
    nombres = ["Ana", "Luis", "Marta", "Pedro"]
    
    for nombre in nombres:
        st.write(nombre)

st.write("Lista de nombres:")
mostrar_lista()


# ==========================================
# 6. BUCLE + CONDICIONAL
# ==========================================

def mostrar_pares():
    
    st.write("Números pares del 1 al 10:")
    
    for i in range(1, 11):
        if i % 2 == 0:
            st.write(i)

if st.button("Ver números pares"):
    mostrar_pares()


# ==========================================
# 7. SELECTOR (interacción)
# ==========================================

opcion = st.selectbox(
    "Elige una opción",
    ["Saludar", "Mostrar números", "Nada"]
)

if opcion == "Saludar":
    st.write("¡Hola!")
elif opcion == "Mostrar números":
    for i in range(5):
        st.write(i)
else:
    st.write("No has elegido nada")


# ==========================================
# 8. FUNCIÓN CON LÓGICA COMPLETA
# ==========================================

def analizar_numeros():
    
    numeros = [3, 7, 2, 9, 4]
    mayores = 0
    
    for num in numeros:
        if num > 5:
            mayores += 1
    
    return mayores

if st.button("Analizar números"):
    resultado = analizar_numeros()
    st.write("Números mayores que 5:", resultado)


# ==========================================
# 9. SLIDER (entrada dinámica)
# ==========================================

numero = st.slider("Elige un número", 0, 20)

st.write("Has elegido:", numero)


# ==========================================
# 10. MINI APP FINAL
# ==========================================

st.subheader("Mini aplicación")

def evaluar_numero(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Impar"

if st.button("Evaluar número"):
    resultado = evaluar_numero(numero)
    st.write("El número es:", resultado)