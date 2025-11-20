# hha_module.py
import streamlit as st

def show_hha_module():
    st.header("🧠 Eje HHA y su relación con la ansiedad")
    st.image("hha_diagram.png", caption="Esquema del eje HHA", use_column_width=True)
    
    with st.expander("🔍 Componentes del eje HHA"):
        st.markdown("""
        - **Hipotálamo**: libera CRH (hormona liberadora de corticotropina)
        - **Hipófisis**: libera ACTH (corticotropina)
        - **Corteza adrenal**: libera cortisol
        """)
    
    with st.expander("⚠️ Alteraciones en TEPT y ansiedad crónica"):
        st.markdown("""
        - Hiperactivación del CRH
        - Retroalimentación negativa alterada
        - Hipercortisolemia sostenida
        - Disfunción emocional y cognitiva
        """)
