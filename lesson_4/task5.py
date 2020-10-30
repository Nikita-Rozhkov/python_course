"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
def my_sum(num):
    num_sum = 0
    for el in num:
        num_sum += float(el)
    return num_sum

with open('file5.txt', 'w+') as file_obj:
    line = input('Введите цифры через пробел \n')
    file_obj.writelines(line)
    numbers = line.split()
    print(my_sum(numbers))
