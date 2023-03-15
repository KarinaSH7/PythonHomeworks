"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""
def indexm(weight, height):
    return weight / (height * height)

def indexr(weight, height):
    result = indexm (weight, height)
    if 18.5 < result < 25:
        print('ИМТ в норме')
    elif result > 25:
        print('Избыточный вес')
    else:
        print('Недостаточный вес')

weight = int(input('введите вес: '))
height = int(input('введите рост: '))

indexr(weight, height)
