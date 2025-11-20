# antidepressants_module.py
import streamlit as st
import pandas as pd

def show_antidepressants_module():
    st.header("💊 Antidepresivos usados en ansiedad")
    
    df = pd.read_excel("antidepresivos_ansiedad.xlsx")
    tipo = st.selectbox("Filtrar por tipo", ["Todos"] + sorted(df["Tipo"].unique()))
    
    if tipo != "Todos":
        df = df[df["Tipo"] == tipo]
    
    st.dataframe(df, use_container_width=True)
    
    with st.expander("📌 Indicaciones clínicas comunes"):
        st.markdown("""
        - **ISRS**: TAG, pánico, fobia social
        - **IRSN**: TAG, dolor crónico con ansiedad
        - **Sedantes**: insomnio con ansiedad o depresión
        """)
