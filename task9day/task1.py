"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""

def para (number1, number2, number3):
    if para != None:
        print(number1, number2, number3)

number1 = int(input())
number2 = int(input())
number3 = int(input())

def three_args(*, var1, var2=None, var3=None):
    arguments = ', '.join([f'{arg[0]} = {str(arg[1])}' for arg in locals().items() if arg[1] is not None])
    print(f'Переданы аргументы: {arguments}')
