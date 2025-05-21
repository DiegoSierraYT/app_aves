import streamlit as st
from sections import clasificacion_aves, aves_disponibles, nuestra_app

st.set_page_config(page_title="Reconocimiento de Aves", layout="wide")

st.markdown("""
    <style>
        .navbar {
            background-color: #f0f2f6;
            padding: 1rem 2rem;
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 999;
            border-bottom: 1px solid #d1d1d1;
        }
        .navbar h1 {
            display: inline-block;
            margin-right: 3rem;
            font-size: 24px;
            color: #262730;
        }
        .navbar .nav-item {
            display: inline-block;
            margin-right: 2rem;
            font-size: 18px;
        }
        .block-container {
            padding-top: 6rem;
        }
    </style>
""", unsafe_allow_html=True)

section = st.radio(
    "Navegación",
    ["Nuestra App", "Información Aves Disponibles", "Clasificación de Aves"],
    horizontal=True
)


if section == "Clasificación de Aves":
    clasificacion_aves.clasificar_ave()
elif section == "Información Aves Disponibles":
    aves_disponibles.mostrar_especies()
elif section == "Nuestra App":
    nuestra_app.mostrar_nuestra_app()
