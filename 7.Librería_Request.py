# ==========================================
# 0. IMPORTAR LIBRERÍAS
# ==========================================

import streamlit as st
import requests


# ==========================================
# 1. FUNCIÓN BÁSICA (API)
# ==========================================

def obtener_chiste():
    url = "https://official-joke-api.appspot.com/random_joke"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return f"{datos['setup']} - {datos['punchline']}"
    else:
        return "Error al obtener el chiste"

st.write("Chiste automático:")
st.write(obtener_chiste())


# ==========================================
# 2. BOTÓN PARA LLAMAR API
# ==========================================

if st.button("Obtener otro chiste"):
    st.write(obtener_chiste())


# ==========================================
# 3. INPUT + API
# ==========================================

nombre = st.text_input("Introduce tu nombre")

def saludar_api(nombre):
    return f"Hola {nombre}, aquí tienes un dato curioso 😄"

if nombre:
    st.write(saludar_api(nombre))


# ==========================================
# 4. API CON PARÁMETROS
# ==========================================

st.subheader("Buscar información de un país")

pais = st.text_input("Introduce un país (ej: Spain)")

def obtener_pais(nombre_pais):
    url = f"https://restcountries.com/v3.1/name/{nombre_pais}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()[0]
        return {
            "Nombre": datos["name"]["common"],
            "Capital": datos.get("capital", ["No disponible"])[0],
            "Región": datos["region"],
            "Población": datos["population"]
        }
    else:
        return None

if pais:
    info = obtener_pais(pais)
    
    if info:
        st.write(info)
    else:
        st.write("País no encontrado")


# ==========================================
# 5. BUCLE CON DATOS API
# ==========================================

if st.button("Mostrar varios chistes"):
    for _ in range(3):
        st.write(obtener_chiste())


# ==========================================
# 6. SELECTOR + API
# ==========================================

opcion = st.selectbox(
    "Elige qué quieres ver",
    ["Chiste", "País", "Nada"]
)

if opcion == "Chiste":
    st.write(obtener_chiste())
elif opcion == "País":
    st.write("Introduce un país arriba 👆")
else:
    st.write("No has elegido nada")


# ==========================================
# 7. MINI APP FINAL
# ==========================================

st.subheader("Mini App API")

if st.button("Dato aleatorio"):
    st.write(obtener_chiste())