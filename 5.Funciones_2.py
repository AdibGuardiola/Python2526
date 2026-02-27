import streamlit as st
import requests
import plotly.express as px
import pandas as pd

# ==========================================
# CONFIG APP
# ==========================================
st.set_page_config(page_title="PIB Mundial", layout="centered")

# ==========================================
# CONSTANTE API
# ==========================================
# en esta url conseguimos el end point    https://datahelpdesk.worldbank.org/knowledgebase/articles/889392
API_URL = "https://api.worldbank.org/v2/country/{}/indicator/NY.GDP.MKTP.CD?format=json"

# ==========================================
# VARIABLE GLOBAL
# ==========================================
paises_default = ["ESP", "USA", "CHN", "DEU"]

# ==========================================
# FORMATEAR PIB
# ==========================================
def formatear_pib(valor):
    if valor >= 1_000_000_000_000:
        return f"{valor/1_000_000_000_000:.2f}T USD"
    elif valor >= 1_000_000_000:
        return f"{valor/1_000_000_000:.2f}B USD"
    else:
        return f"{valor:.2f} USD"

# ==========================================
# CACHE API
# ==========================================
@st.cache_data
def obtener_gdp(country):

    url = API_URL.format(country)

    try:
        response = requests.get(url, timeout=5)
        data = response.json()
    except:
        return None

    if not isinstance(data, list) or len(data) < 2:
        return None

    for item in data[1]:
        if item["value"] is not None:
            return item["value"]

    return None

# ==========================================
# UI
# ==========================================
st.title("PIB por país (World Bank API)")

paises = st.multiselect(
    "Selecciona países",
    ["ESP","USA","CHN","DEU","FRA","ITA","BRA","IND"],
    default=paises_default
)

if st.button("Obtener datos PIB"):

    resultados = []

    for country in paises:

        gdp = obtener_gdp(country)

        if gdp is None:
            st.warning(f"{country}: dato no disponible")
            continue

        gdp = float(gdp)

        st.success(f"{country} tiene PIB {formatear_pib(gdp)}")

        resultados.append((country, gdp))

    # ======================================
    # GRAFICA
    # ======================================
    if resultados:

        df = pd.DataFrame(resultados, columns=["Pais", "PIB"])

        # ranking
        df = df.sort_values("PIB", ascending=False)

        st.subheader("Comparativa PIB")

        fig = px.bar(
            df,
            x="Pais",
            y="PIB",
            text="PIB",
            title="PIB por país"
        )

        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

        st.plotly_chart(fig, use_container_width=True)