# 4.6
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

from itertools import cycle, count

# a)
v_start = int(input("Введите стартовое число:"))
v_end = int(input("Введите конечное число:"))
if v_end < v_start:
    print("Конечное число должно быть больше начального")
else:
    for i in count(v_start):
        if i > v_end:
            break
        else:
            print(i)

# б)
my_list = [1, 3, 5, 7, 9]
c = 0
for el in cycle(my_list):
    if c > 10:
        break
    print(el)
    c += 1