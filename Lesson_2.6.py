# 2.6
# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

i = 0
my_list = []
while True:
    i += 1
    title = input('Введите название товара:')
    price = input('Введите цену товара:')
    col = input('Введите количество товаров:')
    unit = input('Введите единицу измерения товара:')
    my_dict = {"название": title, "цена": price, "количество": col, "ед": unit}
    my_tuple = (i, my_dict)
    my_list.append(my_tuple)
    ans = input('Хотите ввести еще товар?(да/нет):')
    if (ans == 'нет'):
        break
ls_title = []
ls_price = []
ls_col = []
ls_unit = []
for lis in my_list:
    val = list((dict(lis[1])).values())
    ls_title.append(val[0])
    ls_price.append(val[1])
    ls_col.append(val[2])
    ls_unit.append(val[3])
fin_dict = {'название': ls_title, 'цена': ls_price, 'количество': ls_col, 'ед': ls_unit}
print(fin_dict)
