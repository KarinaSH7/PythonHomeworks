""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""
import os
os.mkdir('task4')
os.chdir('task4')

with open('answer.txt', 'w') as file:
    file.write('я выполнил задание')