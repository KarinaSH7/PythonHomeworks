summa = int(input('введите сумму: '))
time = int(input('введите врем: '))
if time > 10 and time < 12:
    print(int(summa/2))
elif time > 20 and time < 22:
    print(int(summa/4))
else:
    print('вы не попадаете под скидку')