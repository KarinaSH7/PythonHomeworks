from task1 import *
while True:
    serch = str(input('введите запрос')).lower()
    if serch.find('рас') != -1:
        timetable()
    elif serch.find('трен') != -1:
        coach()
    elif serch.find('оплт') != -1:
        pay()
    elif serch.find('доку') != -1:
        dock()
    elif serch.find('соцсе') != -1:
        net()
    else:
        print('вы ввели не корректный запрос')