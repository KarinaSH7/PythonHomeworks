number = int(input('введите число: '))
if (number % 10) % 2 == 0:
    if (sum(map(int, str(number)))) % 3 == 0:
        print('делиться на 6')
else:
    print('число не делиться на 6')
