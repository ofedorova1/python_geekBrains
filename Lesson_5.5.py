# 5.5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

ls_num = []
for i in range(20):
    ls_num.append(randint(0, 10))
print("Cумма чисел в файле: ", sum(ls_num))
with open("test_file_5.5.txt", "w", encoding="utf-8") as f:
    for nm in ls_num:
        f.write(str(nm) + " ")
