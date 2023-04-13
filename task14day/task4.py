"""
Разработайте программу, которая будет показывать слово (или слова),
чаще остальных встречающееся в текстовом файле(файл для проверки можно ручками создать).
Сначала пользователь должен ввести имя файла для обработки. После этого вы должны открыть
файл и проанализировать его построчно, разделив при этом строки по
словам и исключив из них пробелы и знаки препинания. Также при подсчете частоты появления слов
в файле вам стоит игнорировать регистры
"""
filename = input("Введите имя файла: ")

with open(filename, "r") as file:
    word_count = {}
    for line in file:
        words = line.strip().split()
        for word in words:
            word = word.lower()
            word = word.strip('.,?!-')
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

most_common_word = max(word_count, key=word_count.get)
print("Самое часто встречающееся слово в файле:", most_common_word)
