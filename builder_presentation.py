import streamlit as st
from streamlit_reveal_slides import slides

def show_builder_presentation():
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
            ## Паттерн Builder (Строитель)
            
            **Порождающий паттерн**, который позволяет создавать сложные объекты пошагово.
            
            ---
            
            ### Когда использовать?
            - Когда объект имеет сложную структуру
            - Когда нужно создавать разные представления одного объекта
            - Когда нужно изолировать код создания объекта от его представления
            """
        )

        slides_placeholder.slide(
            """
            ### Структура паттерна
            
            ```mermaid
            classDiagram
                class Director {
                    -builder: Builder
                    +construct()
                }
                
                class Builder {
                    <<interface>>
                    +build_part_a()
                    +build_part_b()
                    +get_result()
                }
                
                class ConcreteBuilder {
                    +build_part_a()
                    +build_part_b()
                    +get_result()
                }
                
                Director --> Builder
                Builder <|-- ConcreteBuilder
            ```
            """
        )

        slides_placeholder.slide(
            """
            ### Пример реализации на Python
            
            ```python
            class Pizza:
                def __init__(self):
                    self.size = None
                    self.cheese = False
                    self.pepperoni = False
                    self.mushrooms = False
                
                def __str__(self):
                    return (f"Pizza: size={self.size}, "
                            f"cheese={self.cheese}, "
                            f"pepperoni={self.pepperoni}, "
                            f"mushrooms={self.mushrooms}")
            ```
            """
        )

        slides_placeholder.slide(
            """
            ### Класс строителя
            
            ```python
            class PizzaBuilder:
                def __init__(self):
                    self.pizza = Pizza()
                
                def set_size(self, size):
                    self.pizza.size = size
                    return self
                
                def add_cheese(self):
                    self.pizza.cheese = True
                    return self
                
                def add_pepperoni(self):
                    self.pizza.pepperoni = True
                    return self
                
                def add_mushrooms(self):
                    self.pizza.mushrooms = True
                    return self
                
                def build(self):
                    return self.pizza
            ```
            """
        )

        slides_placeholder.slide(
            """
            ### Использование строителя
            
            ```python
            # Создаем строителя
            builder = PizzaBuilder()
            
            # Строим пиццу
            pizza = (builder.set_size("Large")
                      .add_cheese()
                      .add_pepperoni()
                      .build())
            
            print(pizza)
            # Pizza: size=Large, cheese=True, 
            # pepperoni=True, mushrooms=False
            ```
            
            ---
            
            **Преимущества:**
            - Позволяет изменять внутреннее представление продукта
            - Изолирует код создания объекта
            - Дает контроль над процессом конструирования
            """
        )

if __name__ == "__main__":
    show_builder_presentation()
