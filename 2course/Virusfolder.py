"""напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке target,
новые имена придумайте самостоятельно.
"""
import os
os.mkdir('target')


os.chdir('target')
for i in range(1, 11):
    os.mkdir(str(i))

for i in range(2, 11, 2):
    os.rename(str(i), 'virus' + str(i))