import streamlit as st

def show_builder_presentation():
    st.title("🏗️ Паттерн Builder (Строитель)")
    
    # Слайд 1
    st.header("1. Суть паттерна")
    st.markdown("""
    **Builder** позволяет:
    - Создавать объекты **пошагово**
    - Использовать один и тот же код для разных вариантов объекта
    - Изолировать сложную логику создания
    """)
    st.image("https://refactoring.guru/images/patterns/diagrams/builder/structure.png", width=500)
    
    # Разделитель
    st.markdown("---")
    
    # Слайд 2
    st.header("2. Реализация на Python")
    st.code("""
    class Pizza:
        def __init__(self):
            self.size = None
            self.cheese = False
            self.pepperoni = False

    class PizzaBuilder:
        def __init__(self):
            self.pizza = Pizza()
        
        def set_size(self, size):
            self.pizza.size = size
            return self
            
        def add_cheese(self):
            self.pizza.cheese = True
            return self
    """, language='python')
    
    # Разделитель
    st.markdown("---")
    
    # Слайд 3
    st.header("3. Пример использования")
    st.code("""
    builder = PizzaBuilder()
    pizza = (builder
             .set_size("Large")
             .add_cheese()
             .add_pepperoni()
             .build())
    
    print(pizza.size)  # Large
    print(pizza.cheese) # True
    """)
    st.info("💡 Каждый метод возвращает `self` для цепочки вызовов!")

if __name__ == "__main__":
    show_builder_presentation()
