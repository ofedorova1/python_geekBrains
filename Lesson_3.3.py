# 3.3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(var_1, var_2, var_3):
    my_arr = [var_1, var_2, var_3]
    my_arr.remove(min(var_1, var_2, var_3))
    print("Сумма наиболльших чисел:", str(sum(my_arr)))


my_func(float(input("Первое число:")), float(input("Второе число:")), float(input("Третье число:")))
