"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""

def my_range(start,stop,step=1):
    while start <= stop:
        yield start
        start+=step

numbers = my_range(20, 241)
new_list = [el for el in numbers if el%20==0 or el%21==0]
print(new_list)