import streamlit as st
import plotly.express as px

st.title("📊 Ejemplos con Plotly Express")

# ==========================================
# 1. GRÁFICO DE BARRAS
# ==========================================

st.header("1. Gráfico de barras")

nombres = ["Ana", "Luis", "Marta"]
notas = [7, 5, 9]

fig1 = px.bar(x=nombres, y=notas, title="Notas")
st.plotly_chart(fig1)


# ==========================================
# 2. GRÁFICO DE LÍNEAS
# ==========================================

st.header("2. Gráfico de líneas")

dias = [1, 2, 3, 4, 5]
valores = [2, 4, 3, 5, 6]

fig2 = px.line(x=dias, y=valores, title="Progreso")
st.plotly_chart(fig2)


# ==========================================
# 3. GRÁFICO DE DISPERSIÓN
# ==========================================

st.header("3. Gráfico de dispersión")

altura = [150, 160, 170, 180]
peso = [50, 60, 70, 80]

fig3 = px.scatter(x=altura, y=peso, title="Altura vs Peso")
st.plotly_chart(fig3)


# ==========================================
# 4. SELECTOR + GRÁFICO
# ==========================================

st.header("4. Selector interactivo")

asignatura = st.selectbox(
    "Elige asignatura",
    ["Matemáticas", "Lengua"]
)

alumnos = ["A", "B", "C"]

if asignatura == "Matemáticas":
    notas = [5, 6, 7]
else:
    notas = [6, 7, 8]

fig4 = px.bar(x=alumnos, y=notas, title=f"Notas de {asignatura}")
st.plotly_chart(fig4)


# ==========================================
# 5. SLIDER + MINI APP
# ==========================================

st.header("5. Mini app con slider")

cantidad = st.slider("Elige cantidad de números", 1, 10)

lista = list(range(1, cantidad + 1))

fig5 = px.line(x=lista, y=lista, title="Números generados")
st.plotly_chart(fig5)