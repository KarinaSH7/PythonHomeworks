def scene1():
    import time
    print("""ДОБРО ПОЖАЛОВАТЬ В ИГРУ "Любовь в городе"!

        Главная героиня - девушка по имени Анна, которая уже давно влюблена в своего тайного поклонника.
        Она не знает, кто он такой и как выглядит, но каждый день получает от него анонимные сообщения и подарки.
        
        Сегодня её День Рождения и ей доставили загадочное письмо,
        в котором тайный поклонник приглашает приглашает ее на свидание.
        Письмо содержит инструкции, как найти локацию.
        
        У Ани есть два варианта: отправиться на поиски или остаться дома.


        Введите свой вариант: остаться или пойти?
    """)

    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while (ans == 'incorrect'):
        if (c1.upper() == "ОСТАТЬСЯ"):
            print(
                "\nАнна решает остаться дома и отпраздновать свой день рождения с друзьями. К сожалению, ещё долгие годы она не встретит свою настоящую любовь.")
            ans = 'correct'
        elif (c1.upper() == "ПОЙТИ"):
            print("Анна радостно спускается вниз на первый этаж. Весь дом празднично украшен."
                  " Сейчас перед девушкой стоит важный выбор в каком наряде отправиться на поиски своей любви.")
            ans = 'correct'
            scene2()
        else:
            print("ВВЕДИТЕ ПРАВИЛЬНЫЙ ВЫБОР! Остаться или Пойти?")
            c1 = input()


def scene2():
    import time
    print("""
        Она заходит в свой гардероб и выбирает себе образы.
        Останавливается между: черным элегантным платьем с сумочкой BALENCIAGA или в брючном костюме в свело-голубых оттенках.

        Выбери: Платье или Костюм ?

         """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while (ans == 'incorrect'):
        if (c1.upper() == "ПЛАТЬЕ"):
            print(
                "\nВ этом наряде она смотрится невероятно женственной и восхитительно красивой.")
            ans = 'correct'
            scene3()
        elif (c1.upper() == "КОСТЮМ"):
            print("Отличный выбор! В этот наряде она выглядит потрясающе.")
            ans = 'correct'
            scene3()
        else:
            print("ВВЕДИТЕ ПРАВИЛЬНЫЙ ВЫБОР! Платье или Костюм?")
            c1 = input()

def scene3():
        import time
        print("""

        Аня вышла из дома на поиски своего тайного поклонника. На записки было написано:
        "Отправляейся в своё любимое кафе 'Romantic' на Невском и заказажи латте у официанта.".
        """)
        time.sleep(1)
        print("""
        При входе её встретил официант и проводил к столику.
        """)

        c1 = input("""
        Что скажете ему?
        Заказажите латте или спросите не видел ли он тут странного мужчину?
        ВЫБЕРИТЕ: Латте или Вопрос?
        """)
        time.sleep(1)
        ans = 'incorrect'
        while (ans == 'incorrect'):
            if (c1.upper() == "ВОПРОС"):
                print(
                    "\nОфициант ничего не знает про мужчину."
                    "Тогда вы решили следовать инструкции и просто заказали латте. Через несколько минут вам принесли ещё записку: \n В парке сейчас прекрасно, тебя ждёт следующая подсказка именно там. Найди старика на лавочке.")
                ans = 'correct'
                scene4()
            elif (c1.upper() == "ЛАТТЕ"):
                print("""
            Вы заказали латте и через несколько минут вам принесли кофе с ещё одной запиской. Там было написано:
            В парке сейчас прекрасно, тебя ждёт следующая подсказка именно там. Найди старика на лавочке.
                    
            """)
                ans = 'correct'
                scene4()
            else:
                print("ВВЕДИТЕ ПРАВИЛЬНЫЙ ВЫБОР! Латте или Вопрос ")
                c1 = input()


def scene4():
    import time
    print("""
           Аня пришла в парк, там было очень красиво.
           На скамейках сидели дети с родителями, но пройдя чуть дальше по аллее она заметила пожилового старика с тростью.

           Есть два выбора: подойти и попросить подсказку или узнать не видел ли он здесь странного мужчину?
           ВЫБЕРИ: Подсказка или Вопрос ?

            """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while (ans == 'incorrect'):
        if (c1.upper() == "ВОПРОС"):
            print("""
            
            Аня спросила не видел ли дедушка странного мужчину в парке. На что страрик покачал головой."
            Тогда она спросила не знает ли он что-то про подсказку с новой локацией."
            Страрик улыбнулся и протянул ей бумажку, в которой было написано, что в Исаакиевсом соборе тебя ждёт экскурсовод.
            
            """)
            ans = 'correct'
            scene5()
        elif (c1.upper() == "ПОДСКАЗКА"):
            print("Страрик улыбнулся и протянул ей бумажку, в которой было написано,что в Исаакиевсом соборе тебя ждёт экскурсовод.")
            ans = 'correct'
            scene5()
        else:
            print("ВВЕДИТЕ ПРАВИЛЬНЫЙ ВЫБОР! Подсказка или Вопрос? ")
            c1 = input()

def scene5():
    import time
    print("""

           Аня пошла в Исаакиевский. Это грандиозное архитектурное сооружение сверкало в лучах солнце и выглядило великолепно.
           Она поднялась по ступенькамм и открыла дверь, на входе было несколько групп туристов, которые ждали начала экскурсии. К Ане подошёл экскурсовод и спросил нужна ли ей помощь?
        """)
    time.sleep(1)
    print("""
           Девушка посмотела на него. И хотела задать вопрос.
           Один из которых был про то, не знает ли экускурсовод что-то про старанного мужчину или не передвал ему кто-то конверст с запиской?
        
           ВЫБЕРИ: Вопрос или Записка ?
        """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while (ans == 'incorrect'):
        if (c1.upper() == "ВОПРОС"):
            print("""

            Экскурсовод сказал, что он никого не видел, но его коллега попросил передать Вам конверт.
            Он достал конверт и протянул его. Внутри лежала финальная запсика: 'Подниимайся на самую высокую точку этого здания.

                """)
            ans = 'correct'
            scene6()
        elif (c1.upper() == "ЗАПИСКА"):
            print("""
            Экскурсовд отошёл за стойку и достал от туда конверт, внути котрого лежала финальная записка.
            В ней было написано: 'Подниимайся на самую высокую точку этого здания.
            """)
            ans = 'correct'
            scene6()
        else:
            print("ВВЕДИТЕ ПРАВИЛЬНЫЙ ВЫБОР! Вопрос или Записка? ")
            c1 = input()



def scene6():
    import time
    print("""

           Аня вспомнила про самую красивую понармную площадку и повернув направо к лестнице,
           которая вела наверх, она начала подниматься по ступенькам.
       """)
    time.sleep(1)
    print("""
           Поднявшись она уидела потрясающий вид на весь Санкт-Перербург и праздничный стол на двоих.""")

    print("""
           Рядом со смотровой площадкой стоял парень. """)

    time.sleep(2)
    print("""
           Он был одет в костюм и не снимал маску.
           """)
    time.sleep(2)
    print("Он заговорил:")
    time.sleep(2)
    print("- Аня я все время был рядом. Я боялся признаться в своих чувствах, но я люблю тебя.")
    time.sleep(2)
    print("- Кто ты такой? - спросила Анна.")
    time.sleep(2)
    print("- Это я, твой лучший друг. Я всегда был рядом и помогал тебе в трудные моменты.")
    time.sleep(2)
    print("- Я не могу поверить. - сказала Анна.")
    time.sleep(2)
    print("- Ты можешь сделать что-то для меня? - спросил друг.")
    time.sleep(2)
    print("- Да, конечно.")
    time.sleep(2)
    print("- Стать моей девушкой.")
    time.sleep(2)
    print("- Я думаю...да.")
    time.sleep(2)
    print("Друг и Анна поцеловались, тем самым став парой.")

print("\nКонец игры!")
scene1()
print("\n\n")
print("=================================THE END=================================")


