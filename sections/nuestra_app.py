import streamlit as st
import os

def mostrar_nuestra_app():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    imagen_path = os.path.join(base_dir, "../recursos/portada.png")

    st.markdown("<h1 style='text-align: center; color: #3a5f0b;'>Plumas del Tolima</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: gray;'>Reconocimiento de aves del Tolima mediante visión por computador</h4>", unsafe_allow_html=True)
    st.markdown("")

    st.image(imagen_path, use_container_width=True, caption="Aves del departamento del Tolima")

    st.markdown("## 🌿 Acerca del proyecto")
    st.write("""
Tolibird es una herramienta interactiva que aprovecha el poder del aprendizaje profundo para **identificar aves nativas del Tolima** a partir de imágenes. Diseñada con un enfoque educativo y ecológico, esta aplicación busca fomentar el conocimiento y la conservación de la biodiversidad regional.
    """)

    st.markdown("## ⚙️ ¿Qué puedes hacer aquí?")
    st.write("""
- Subir una imagen de un ave para conocer su posible especie  
- Consultar el nombre científico y estado de conservación  
- Visualizar imágenes de referencia por especie  
- Conocer más sobre las aves del ecosistema tolimense  
    """)

    st.markdown("## 🚀 ¿Cómo empezar?")
    st.write("""
1. Dirígete al menú superior y selecciona **Clasificación de Aves**  
2. Carga una imagen en buena calidad del ave  
3. Revisa las 3 predicciones más probables del modelo  
4. Explora más detalles sobre cada especie sugerida  
    """)

    st.markdown("---")
