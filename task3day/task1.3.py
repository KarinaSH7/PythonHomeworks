money1 = int(input('сумма товара 1: '))
money2 = int(input('сумма товара 2: '))
money3 = int(input('сумма товара 3: '))
summa = money1 + money2 + money3
if money1 > money2 and money2 > money3:
    print('Акция!', (summa)/2)
elif money1 < money2 and money2 < money3:
    print('Акция!', (summa)/3)
else:
    print('К оплате: ', (summa))