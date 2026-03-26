import streamlit as st
import random

st.set_page_config(
    page_title="Piedra Papel o Tijera",
    page_icon="✂️",
    layout="centered"
)

st.title("✊ Piedra, Papel o Tijera")
st.write("Mi segundo intento usando Streamlit")

# Elección del usuario
usuario = st.selectbox(
    "Elige una opción",
    ["piedra", "papel", "tijera"]
)

# Botón para jugar
if st.button("Jugar"):

    opciones = ["piedra", "papel", "tijera"]
    computadora = random.choice(opciones)

    st.write(f"💻 Computadora eligió: {computadora}")

    # Lógica del juego
    if usuario == computadora:
        st.info("Empate 🤝")

    elif (
        (usuario == "piedra" and computadora == "tijera") or
        (usuario == "papel" and computadora == "piedra") or
        (usuario == "tijera" and computadora == "papel")
    ):
        st.success("¡Ganaste! 🎉")

    else:
        st.error("Perdiste 😢")

