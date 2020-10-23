"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(name, surname, birth_year, city, email, phone_number):
    data = ' '.join([name, surname, birth_year, city, email, phone_number])
    return data

user_name=input("Bведите имя \n")
user_surname=input("Bведите фамилию \n")
user_year=input("Введите год рождения \n")
user_city=input("Введите город \n")
user_email=input("Введите адрес электронной почты \n")
user_phone=input("Введите адрес номер телефона \n")
print(f"Данные пользователя: {user_data(user_name,user_surname,user_year,user_city,user_email,user_phone)}")





