"""
Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

lines_list = ['Abcd\n', 'Efgh\n', 'Ijkl\n']
with open("file2.txt", 'w+') as file_obj:
    file_obj.writelines(lines_list)
with open("file2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"Количество букв в строке:{letters}")
    print(f"Количество строк: {lines}")