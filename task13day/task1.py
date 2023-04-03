"""
Напишите генератор выводящий все символы строки на печать, но только в том случае, если они являются буквами (остальные игнорируются).
"""

def generator(string):
    for words in string:
        if words.isalpha():
            yield words

strings = input("Введите предложение: ")
for letter in generator(strings):
    print(letter, end='')