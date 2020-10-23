"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def division (number_1, number_2):
    try:
        result = number_1 / number_2
        return result
    except ZeroDivisionError:
        return "Делить на ноль нельзя!"
    except ValueError:
        return "Нельзя вводить символы"
mynumber_1=int(input("Введите первое число "))
mynumber_2=int(input("Введите второе число "))
print(f"Результат деления {mynumber_1} на {mynumber_2} равен {division(mynumber_1,mynumber_2)}")