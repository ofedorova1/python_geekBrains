# 3.5
# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def my_fun(v_inp):
    """Подсчет суммы последовательности"""
    v_sum = 0
    while True:
        """При первом вводе значения передаются из функции fin_function()"""
        if v_inp != "":
            v_str = v_inp
            v_inp = ""
        else:
            """Ввод последующих наборов цифр"""
            v_str = input()

        ar_num = (str(v_str)).split(" ")
        """Подсчет суммы"""
        for i in range(len(ar_num)):
            if ar_num[i].isdigit():
                v_sum = v_sum + float(ar_num[i])
            else:
                return v_sum
        print(v_sum)


def fin_function():
    """Вывод общей суммы"""
    v_inp = (input("Введите последовательность (для выхода из программы введите 'Q'):"))
    if str(v_inp).upper() == "Q":
        return print("Суммы не случилось...")
    else:
        print("Общая сумма", my_fun(v_inp))


fin_function()
