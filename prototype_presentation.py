import streamlit as st

def show_prototype_presentation():
    st.title("🎯 Паттерн Prototype (Прототип)")
    
    # Слайд 1
    st.header("1. Что это?")
    st.markdown("""
    **Prototype** — это порождающий паттерн, который:
    - Позволяет копировать объекты **без привязки к их классам**
    - Упрощает создание сложных объектов
    - Работает через метод `clone()`
    """)
    st.image("https://refactoring.guru/images/patterns/diagrams/prototype/structure.png", width=500)
    
    # Разделитель
    st.markdown("---")
    
    # Слайд 2
    st.header("2. Пример кода")
    st.code("""
    import copy

    class Prototype:
        def clone(self):
            return copy.deepcopy(self)

    class Car(Prototype):
        def __init__(self, model, color):
            self.model = model
            self.color = color
    """, language='python')
    
    # Разделитель
    st.markdown("---")
    
    # Слайд 3
    st.header("3. Как использовать?")
    st.code("""
    # Создаем оригинал
    tesla = Car("Model S", "red")
    
    # Клонируем и меняем
    cloned_tesla = tesla.clone()
    cloned_tesla.color = "blue"
    
    print(tesla.color)        # red
    print(cloned_tesla.color) # blue
    """)
    st.success("✅ Клон независим от оригинала!")

if __name__ == "__main__":
    show_prototype_presentation()
