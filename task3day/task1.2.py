summa = int(input('введите сумму: '))
time = int(input('введите врем: '))
if 10 < time < 12:
    print(int(summa / 2))
elif 20 < time < 22:
    print(int(summa / 4))
else:
    print('вы не попадаете под скидку')
