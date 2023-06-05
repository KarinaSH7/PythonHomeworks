"""Реализуйте класс Алхимия который принимает  элемент в виде строки. Класс должен содержать метод объединения
(переопределение оператора +), который возвращает новый элемент в виде строки где первые 3 буквы от первого элемента и 3 последнии от второго.
Метод сложный элемент(переопределение оператора умножения) который возвращает 3 первые буквы первого элемента
умноженные на количество букв второго элемента. Метод постепенного уничтожения который при вызове стирает 1 букву названия с конца.
Создайте 2 элемента и продемонстрируйте работу каждого метода.
"""

class Alchemy:
    def __init__(self, element):
        self.element = element

    def __add__(self, other):
        return self.element[:3] + other.element[-3:]

    def __mul__(self, other):
        return self.element[:3] * len(other.element)

    def destruction(self):
        self.element = self.element[:-1]

elem1 = Alchemy("oxygen")
elem2 = Alchemy("gold")

print(elem1 + elem2)
print(elem1 * elem2)
elem1.destruction()
print(elem1.element)
elem1.destruction()
print(elem1.element)