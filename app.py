import streamlit as st

# Configuración básica de la página
st.set_page_config(
    page_title="Calculadora",
    page_icon="🧮",
    layout="centered"
)

# Título y texto
st.title("🧮 Calculadora básica")
st.write("Mi primera interfaz web en Python con Streamlit")


col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Primer número", value=0.0, format="%0.2f")

with col2:
    num2 = st.number_input("Segundo número", value=0.0, format="%0.2f")

# Lista desplegable para elegir operación
operacion = st.selectbox(
    "Selecciona una operación",
    ["Suma", "Resta", "Multiplicación", "División"]
)

# Botón para calcular
if st.button("Calcular"):
    if operacion == "Suma":
        resultado = num1 + num2
        st.success(f"Resultado: {resultado}")

    elif operacion == "Resta":
        resultado = num1 - num2
        st.success(f"Resultado: {resultado}")

    elif operacion == "Multiplicación":
        resultado = num1 * num2
        st.success(f"Resultado: {resultado}")

    elif operacion == "División":
        if num2 == 0:
            st.error("No se puede dividir entre cero")
        else:
            resultado = num1 / num2
            st.success(f"Resultado: {resultado}")