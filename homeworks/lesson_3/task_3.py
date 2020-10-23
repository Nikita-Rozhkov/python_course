"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""
def max_sum(number_1 , number_2, number_3):
    if number_1 >= number_3 and number_2 >= number_3:
        return number_1 + number_2
    elif number_1 > number_2 and number_1 < number_3:
        return number_1 + number_3
    else:
        return number_2 + number_3
mynumber_1=int(input("Введите первое число"))
mynumber_2=int(input("Введите второе число"))
mynumber_3=int(input("Введите третье число"))
print(f"Сумма двух наибольших чисел: {max_sum(mynumber_1,mynumber_2,mynumber_3)}")