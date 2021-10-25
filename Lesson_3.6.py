# 3.6
# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
def int_function(v_input):
    my_str = ""
    """Строка разделяется на слова"""
    arr_inp = str(v_input).split(" ")
    for i in range(len(arr_inp)):
        """Слово разделяется на буквы"""
        ls_letter = list(arr_inp[i])
        arr_tmp = []
        for j in range(len(ls_letter)):
            """Проверка, являются ли буквы латинскими в нижнем регистре"""
            if 97 <= ord(ls_letter[j]) and ord(ls_letter[j]) <= 122:
                arr_tmp.append(ls_letter[j])
        if len(arr_tmp) == len(arr_inp[i]):
            my_str = my_str + " " + str(arr_inp[i])
    my_str = my_str.title()
    print(my_str)


int_function(input("Введите строку слов через пробел:"))
