"""
1 функция - принимает имя и количество положительных оценок
 и заносит в словарь ключ-имя значение-количество оценок
2 функция принимает строку/имя и выводит количество оценок

"""
marks_dict = {}
name = input("")
marks = input()


def student(name, marks):
    marks_dict[name] = marks


def print_marks(name):
    if name in marks_dict:
        print(f"{name}  {marks_dict[name]} .")
    else:
        print(f"{name} нет оценок.")


student(name, len(marks))
print_marks(name)
