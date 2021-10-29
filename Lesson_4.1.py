# 4.1
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами

from sys import argv

script_name, w_hour, m_hour, bonus = argv


def get_salary(w_hour, m_hour, bonus):
    print("Заработна плата:", round(float(w_hour) * float(m_hour) + float(bonus), 3))


get_salary(w_hour, m_hour, bonus)
