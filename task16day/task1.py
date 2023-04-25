"""
Напишите программу которая будет спрашивать пользователя ввод имени пока пользователь не введет off.
Программа должна используя lambda-функцию добавлять к каждому имени надпись "гений".
"""
people = []
while True:
    name = input("Введите имя: ")
    if name == "off":
        break
    people.append(name)

genius_names = list(map(lambda x: "гений " + x, people))

print(genius_names)