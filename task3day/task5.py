print('Приветсвуем тебя в магазине "Кристалл" сегодня у нас дейсвует скидка 20% от любой покупки')
while True:
    cost = float(input('Введите стоимость покупки: '))
    if cost == 0:
        break
    discount = (cost/100)*20
    difference = cost - discount
    print(f'скидка: {discount}')
    print(f'к оплате: {difference}')

print('Спасибо за покупку!')
