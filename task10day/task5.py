"""
Напишите программу-имитатор подбрасывания 2 кубиков.
Программа выводит на экран "подбрасываю кубики" и спустя 2 секунды выводит значения на кубиках в одну строку.
"""
import random
import time

print('ИГРА В КУБИКИ НАЧАЛАСЬ\n''подбрасываю кубики')
time.sleep(2)
random_number1 = random.randint(1, 6)
random_number2 = random.randint(1, 6)
print('Вам выпали числа: ', random_number1, random_number2)
