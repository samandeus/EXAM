import streamlit as st
from prototype_presentation import show_prototype_presentation
from builder_presentation import show_builder_presentation

st.set_page_config(page_title="Паттерны проектирования", layout="wide")

# Меню выбора
st.sidebar.title("🔍 Выбери паттерн")
choice = st.sidebar.radio("", ["Prototype", "Builder"])

if choice == "Prototype":
    show_prototype_presentation()
else:
    show_builder_presentation()
