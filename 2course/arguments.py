"""
Напишите скрипт который принимает 2 аргумента и записывает первый аргумент в файл где имя файла второй аргумент.
"""

import sys

if len(sys.argv) == 3:
    filename = sys.argv[2]
    with open(filename, 'w') as f:
        f.write(sys.argv[1])
    print(f"argument '{sys.argv[1]}' write in file {filename}")
else:
    print('incorrect number of arguments')


