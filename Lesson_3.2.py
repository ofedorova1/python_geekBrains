# 3.2
# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(var_city, var_surname, var_year, var_email, var_tel, var_name):
    print(var_name, var_surname, var_year, var_city, var_email, var_tel)


my_func(var_name=input("Введите имя:"), var_surname=input("Введите фамилию:"),
        var_year=input("Введите год рождения:"),
        var_city=input("Введите город проживания:"), var_email=input("Введите email:"),
        var_tel=input("Введите телефон:"))
