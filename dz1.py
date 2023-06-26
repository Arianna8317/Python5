#Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
#Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def file_path_parser(file_path):
    path, file = os.path.split(file_path)
    name, ext = os.path.splitext(file)
    return (path, name, ext)


path, name, ext = file_path_parser('Python/Advanced/Homework/test.py')
print(f'Path: {path}')
print(f'Name: {name}')
print(f'Ext: {ext}')