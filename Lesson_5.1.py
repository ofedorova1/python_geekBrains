# 5.1
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка
my_file = open("test_file_5.1.txt", "w", encoding="utf-8")
str_list = []
while True:
    inp = input("Введите данные:")
    if inp != "":
        str_list.append(inp + '\n')
    else:
        break
my_file.writelines(str_list)
my_file.close()
