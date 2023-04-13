"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""
my_fil = open("B.txt", "r")
text = my_fil.read()
my_fil.close()
print(text)
my_file = open("A.txt", "w+")
my_file.write(text+" но у меня не получается")
my_file.seek(0)
new_text = my_file.read()
print(new_text)
with open('combined.txt', 'w') as f3:
    f3.write(new_text)
my_file.close()
