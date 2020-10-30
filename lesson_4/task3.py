"""
 Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
 Определить, кто из сотрудников имеет оклад менее 20 тыс.,
 вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""
company = {'Employee_1': 18000, 'Employee_2': 21000, 'Employee_3': 17000, 'Employee_4': 23000}
try:
    file_obj = open("file3.txt", 'w')
    for name, salary in company.items():
        file_obj.write(name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
salary_sum = 0
count = 0
persons = []
with open("file3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        lines = line.split(':')
        if int(lines[1]) <= 20000:
            persons.append(lines[0])
        salary_sum += int(lines[1])
        count += 1
result = salary_sum / count
print(f"Сотрудники с низким окладом: {persons}")
print(f"Средний доход: {result}")
