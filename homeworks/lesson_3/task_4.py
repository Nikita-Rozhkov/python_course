"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""
def neg_power(number, power):

    if power < 0:
        cur_power = 1
        res = 1
        while cur_power <= abs(power):
            res*=number
            cur_power+=1
        result = 1 / res
    else:
        print("Степень должна быть отрицательной")
    return result

mynumber = float(input("Введите основание степени"))
mypower = int(input("Введите отрицательный показатель степени"))
print(neg_power(mynumber, mypower))





