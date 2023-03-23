"""
Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму опла-
ты такси.
"""


def taxi(kilom):
    return (round((4 + 0.25 * kilom / 140), 2))


kilom = int(input("Введите расстояние поездки: "))
print('Стоимость поездки: ', taxi(kilom))