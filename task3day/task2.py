while True:
    words = input('Введите game или off: ')
    if words == 'off':
        break
    elif words == 'game':
        print('"Угадай число" У тебя есть 3 попытки, вводи число: ')
        for i in range(0, 3):
            number = int(input())
            if number == 5:
                print('Вы выиграли билеты на концерт!')
                break
            else:
                print('У тебя осталось несколько попыток! ')
                continue
        else:
            print('Попытки кончились')
            continue
