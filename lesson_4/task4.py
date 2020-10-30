"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

rus = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'cчетыре'}
result = []
try:
    file_obj = open("file4.txt", 'r')
    for line in file_obj:
        el = line.split(" - ")
        print(el)
        if el[0] in rus:
            word = rus[el[0]]
            result.append(word +' - '+ el[1])
    print(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
try:
    file_new = open("file4_new.txt", "w")
    file_new.writelines(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_new.close()