"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

def my_range(start,stop,step=1):
    while start <= stop:
        yield start
        start+=step

def my_reduce(function, elements):
    for idx in my_range(1,len(elements)):
        elements[idx]=function(elements[idx-1], elements[idx])
    return elements[len(elements) - 1]

def my_func(prev_el, el):
    return prev_el * el

my_list = [el for el in my_range(100, 1001) if el % 2 == 0]
print(my_reduce(my_func, my_list))
