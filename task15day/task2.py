"""
Напишите программу добавляющую в рецепт бутерброда ингридиенты "Салат" и "Ананасы" с помощью декораторов.
"""

def add_salad(func):
    def wrapper():
        sandwich = func()
        sandwich += " + Salad"
        return sandwich
    return wrapper

def add_pineapple(func):
    def wrapper():
        sandwich = func()
        sandwich += " + Pineapple"
        return sandwich
    return wrapper

@add_salad
@add_pineapple
def make_sandwich():
    return "Bread"

print(make_sandwich())
