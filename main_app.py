import streamlit as st
from prototype_presentation import show_prototype_presentation
from builder_presentation import show_builder_presentation

st.set_page_config(page_title="Паттерны проектирования", layout="wide")

# Создаем навигацию
st.sidebar.title("Навигация")
page = st.sidebar.radio("Выберите презентацию:", 
                        ["Prototype", "Builder"])

if page == "Prototype":
    show_prototype_presentation()
elif page == "Builder":
    show_builder_presentation()
