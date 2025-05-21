import streamlit as st
import numpy as np
import cv2
import os
import pandas as pd
from keras.applications.imagenet_utils import preprocess_input
from PIL import Image
from utils.model_loader import cargar_modelo

def clasificar_ave():
    st.title("🕊️ Clasificador de Aves - VGG16")

    base_dir = os.path.dirname(os.path.abspath(__file__))

    ruta_modelo = os.path.join(base_dir, "../model_VGG16_v2_os.keras")
    excel_path = os.path.join(base_dir, "../recursos/clases_aves.xlsx")
    imagenes_base = os.path.join(base_dir, "../recursos/imagenes")

    names = ['Dacnis Azul','Mielerito Cerúleo','Mielero Patas Rojas','Mielero Verde','Tangara Guirá',
             'Tangara Gorjigualda','Conirrostro Orejiblanco','Conirrostro Dorsiazul','Conirrostro Coronado',
             'Clorospingo Gorjiamarillo','Eufonia sp_','Eufonia Ventricanela','Eufonia Ventrinaranja','Jilguerito Dominico',
             'Jilguero Andino','Jilguero Encapuchado','Jilguero Ventriamarillo','Spinus sp_','Tangara Pecho Rosa']

    try:
        model = cargar_modelo(ruta_modelo)
    except Exception as e:
        st.error(f"❌ Error al cargar el modelo de predicción: {e}")
        return

    try:
        df = pd.read_excel(excel_path)
    except Exception as e:
        st.warning("⚠️ No se encontró el archivo de base de datos con información de las aves.")
        df = None

    uploaded_file = st.file_uploader("📤 Sube una imagen para clasificar", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        try:
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            image = cv2.imdecode(file_bytes, 1)
            resized_image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
            x = preprocess_input(np.expand_dims(resized_image, axis=0))

            st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="📸 Imagen cargada", width=224)
            st.info("🔍 Realizando predicción...")

            preds = model.predict(x)
            top_indices = np.argsort(preds[0])[-3:][::-1] 

            st.success("✅ Top 3 predicciones:")

            for rank, idx in enumerate(top_indices, start=1):
                nombre_ave = names[idx]
                confianza = preds[0][idx] * 100

                st.markdown(f"""
                <div style="padding:15px; border-radius:10px; border:1px solid #d3d3d3; margin-bottom:15px;">
                    <h4 style="color:#4B8BBE;">#{rank} - {nombre_ave} <span style="color:gray;">({confianza:.2f}%)</span></h4>
                """, unsafe_allow_html=True)

                if df is not None and idx < len(df):
                    row = df.iloc[idx]
                    nombre_cientifico_url = row['nombrecientifico'].replace(" ", "+")
                    st.markdown(f"""
                        <p><strong>🧬 Nombre científico:</strong> <em>{row['nombrecientifico']}</em></p>
                        <p><strong>🛡️ Estado de conservación:</strong> {row['estadoconservacion']}</p>
                        <p><a href="https://www.google.com/search?q={nombre_cientifico_url}" target="_blank" style="color:#1a73e8; text-decoration:none;">🔍 Buscar en Google</a></p>
                    """, unsafe_allow_html=True)

                clase_dir = os.path.join(imagenes_base, f"clase{idx + 1}")
                if os.path.exists(clase_dir):
                    imagenes = sorted([
                        f for f in os.listdir(clase_dir)
                        if f.lower().endswith(('.png', '.jpg', '.jpeg'))
                    ])
                    if imagenes:
                        imagenes_mostrar = imagenes[:3]
                        cols = st.columns(len(imagenes_mostrar))
                        for col, nombre_imagen in zip(cols, imagenes_mostrar):
                            img_path = os.path.join(clase_dir, nombre_imagen)
                            img = Image.open(img_path).copy()
                            col.image(img, use_container_width=True, caption=nombre_imagen)
                    else:
                        st.warning("⚠️ No hay imágenes disponibles para esta clase.")
                else:
                    st.warning("⚠️ No se encontró la carpeta de imágenes para esta clase.")

                st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("---")

        except Exception as e:
            st.error(f"❌ Error al procesar la imagen: {e}")
