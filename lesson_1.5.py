# 1.5
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = float(input("Введите сумму выручки:"))
costs = float(input("Введите сумму издержек:"))
if proceeds > costs:
    print("Фирма работает с прибылью.")
    rent = ((proceeds - costs) / proceeds) * 100
    print("Рентабельность фирмы", rent, "%")
    cpeople = int(input("Введите численность сотрудников фирмы:"))
    onepeople = (proceeds - costs) / cpeople
    print("Прибыль на одного человека составляет:", onepeople)
elif proceeds == costs:
    print("Фирма работает в ноль.")
else:
    print("Фирма работает в убыток.")
