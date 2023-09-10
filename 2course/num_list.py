"""
Напишите функцию которая будет принимать список чисел и выводить на экран надпись "сегодня x градусов" столько раз
сколько значений в списке.
"""

degrees_list = [34, 56, 78]


def print_temperature(degrees_list):
    for degrees in degrees_list:
        print(f"Сегодня {degrees} градусов")


print_temperature(degrees_list)
