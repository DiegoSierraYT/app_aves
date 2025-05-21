import streamlit as st
import pandas as pd
import os
from PIL import Image

def mostrar_especies():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    ruta_excel = os.path.join(base_dir, "../recursos/clases_aves.xlsx")
    ruta_imagenes = os.path.join(base_dir, "../recursos/imagenes")

    df = pd.read_excel(ruta_excel)

    st.title("🕊️ Aves Disponibles")

    for idx, row in df.iterrows():
        st.markdown("---")
        
        st.subheader(f"🐦 {row['nombrecomun']} (*{row['nombrecientifico']}*)")

        clase_dir = os.path.join(ruta_imagenes, f"clase{idx + 1}")
        if os.path.exists(clase_dir):
            imagenes = sorted([
                f for f in os.listdir(clase_dir)
                if f.lower().endswith(('.png', '.jpg', '.jpeg'))
            ])[:4]

            cols = st.columns(4)
            for i, img_name in enumerate(imagenes):
                img_path = os.path.join(clase_dir, img_name)
                image = Image.open(img_path).copy()
                cols[i].image(image, caption=f"📸 {img_name}", use_container_width=True)
        else:
            st.warning(f"🚫 No se encontró la carpeta para clase{idx + 1}")

        st.markdown(f"**📝 Descripción:** {row['descripcion']}")
        st.markdown(f"**🌍 Distribución:** {row['distribucion']}")
        st.markdown(f"**⚠️ Estado de conservación:** {row['estadoconservacion']}")

        url_google_nombre = row['nombrecientifico'].replace(" ", "+")
        busqueda_google = f"https://www.google.com/search?q={url_google_nombre}"
        st.markdown(f"[🔎 Buscar en Google]({busqueda_google})")

    st.markdown("---")
