# 2.5
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
my_list = [7, 5, 3, 3, 2]
numb = int(input('Введите натуральное число:'))
if numb > my_list[0]:
    my_list.insert(0, numb)
elif numb < my_list[-1]:
    my_list.append(numb)
else:
    for i in range(len(my_list)):
        if my_list[i] == numb:
            reversed_list_index = my_list[::-1].index(numb)
            idx = len(my_list) - 1 - reversed_list_index
            my_list.insert(idx, numb)
            break
        else:
            if my_list[i] > numb and my_list[i + 1] < numb:
                my_list.insert(i + 1, numb)
                break
print(my_list)
