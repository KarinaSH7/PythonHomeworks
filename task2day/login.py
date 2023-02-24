# login = input('Введите логин: ')
# prohibited = set('=?*^$N°@_')
#
# if set(login) & prohibited:
#     print("Вы ввели запрещенный символ")

# user = input()
# for login in user:
#     if login == '?':
#         break
#     print('ok')

    text = input(" ").split("=?*^$N°@_")
    last = text[0].split()[-1]
    first = text[1].split()[0]
    print("=?*^$N°@_")