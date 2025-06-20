import streamlit as st
from streamlit_reveal_slides import slides

def show_prototype_presentation():
    slides_config = {
        "height": 700,
        "margin": 0.1,
        "transition": "slide",
        "backgroundTransition": "fade",
        "controls": True,
        "progress": True,
        "center": True,
    }

    with slides(slides_config=slides_config, markdown=True) as slides_placeholder:
        slides_placeholder.slide(
            """
            ## Паттерн Prototype (Прототип)
            
            **Порождающий паттерн проектирования**, который позволяет копировать объекты, не вдаваясь в подробности их реализации.
            
            ---
            
            ### Когда использовать?
            - Когда код не должен зависеть от классов копируемых объектов
            - Когда нужно избежать построения иерархий классов фабрик
            """
        )

        slides_placeholder.slide(
            """
            ### Структура паттерна
            
            ```mermaid
            classDiagram
                class Prototype {
                    <<interface>>
                    +clone() Prototype
                }
                
                class ConcretePrototype1 {
                    +clone() Prototype
                }
                
                class ConcretePrototype2 {
                    +clone() Prototype
                }
                
                Prototype <|-- ConcretePrototype1
                Prototype <|-- ConcretePrototype2
            ```
            """
        )

        slides_placeholder.slide(
            """
            ### Пример реализации на Python
            
            ```python
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
            ```
            """
        )

        slides_placeholder.slide(
            """
            ### Использование прототипа
            
            ```python
            # Создаем оригинальный объект
            original_car = Car("Tesla Model S", "red")
            
            # Клонируем объект
            cloned_car = original_car.clone()
            cloned_car.color = "blue"
            
            print(original_car)  # red Tesla Model S
            print(cloned_car)    # blue Tesla Model S
            ```
            
            ---
            
            **Преимущества:**
            - Упрощает создание сложных объектов
            - Избегает повторной инициализации
            - Гибкость в добавлении новых объектов
            """
        )

if __name__ == "__main__":
    show_prototype_presentation()
