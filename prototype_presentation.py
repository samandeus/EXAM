import streamlit as st

def show_prototype_presentation():
    st.title("Паттерн Prototype (Прототип)")
    
    with st.expander("Описание"):
        st.write("""
        **Порождающий паттерн проектирования**, который позволяет копировать объекты, 
        не вдаваясь в подробности их реализации.
        """)
        
        st.write("**Когда использовать?**")
        st.write("- Когда код не должен зависеть от классов копируемых объектов")
        st.write("- Когда нужно избежать построения иерархий классов фабрик")
    
    with st.expander("Структура паттерна"):
        st.image("https://refactoring.guru/images/patterns/diagrams/prototype/structure.png", 
                caption="Структура паттерна Prototype")
    
    with st.expander("Пример реализации"):
        st.code("""
        import copy
        
        class Prototype:
            def clone(self):
                return copy.deepcopy(self)
        
        class Car(Prototype):
            def __init__(self, model, color):
                self.model = model
                self.color = color
            
            def __str__(self):
                return f"{self.color} {self.model}"
        """)
    
    with st.expander("Использование"):
        st.code("""
        # Создаем оригинальный объект
        original_car = Car("Tesla Model S", "red")
        
        # Клонируем объект
        cloned_car = original_car.clone()
        cloned_car.color = "blue"
        
        print(original_car)  # red Tesla Model S
        print(cloned_car)    # blue Tesla Model S
        """)

if __name__ == "__main__":
    show_prototype_presentation()
