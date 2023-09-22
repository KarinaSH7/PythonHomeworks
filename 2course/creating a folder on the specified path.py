"""
Напишите скрипт который принимает 2 аргумента - путь и имя папки. И создаем папку по указанному пути.
"""

import sys
import os

if len(sys.argv) == 3:
    path = sys.argv[1]
    folder_name = sys.argv[2]
    folder_path = os.path.join(path, folder_name)
    os.makedirs(folder_path)
    print(f"folder {folder_name} created along the way {path}")
else:
    print('invalid number of arguments')