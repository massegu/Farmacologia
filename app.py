# app.py
import streamlit as st
from hha_modulo import show_hha_module
from antidepresivos import show_antidepressants_module
from mechanism_module import show_mechanism_module

st.set_page_config(page_title="Neurofarmacología Clínica", layout="wide")

st.sidebar.title("🧠 Módulos")
module = st.sidebar.radio("Selecciona un módulo", ["Eje HHA", "Antidepresivos", "Mecanismo de acción"])

if module == "Eje HHA":
    show_hha_module()
elif module == "Antidepresivos":
    show_antidepressants_module()
elif module == "Mecanismo de acción":
    show_mechanism_module()
