"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

list_length = int(input("Введите количество элементов списка "))
my_list = []
i = 0
el = 0
while i < list_length:
    my_list.append(input("Введите следующее значение списка "))
    i += 1
if list_length % 2 == 0:
    i = 0
    while i < list_length:
        el = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = el
        i += 2
else:
    i = 0
    while i < list_length - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
    print(my_list)

