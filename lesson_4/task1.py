"""
Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

file_obj = open('file1.txt', 'w')
line = input('Введите текст \n')
while line:
    file_obj.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break
file_obj.close()
file_obj = open('file1.txt', 'r')
content = file_obj.readlines()
print(content)
file_obj.close()