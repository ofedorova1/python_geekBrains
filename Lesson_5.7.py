# 5.7
# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

with open("test_file_5.7.txt", "r", encoding="utf-8") as f:
    dc_firms = {}
    l_aver = []
    dc_aver = {}
    ls_fin = []
    for line in f:
        words = line.split()
        f_name = words[0]
        v_proceeds = int(words[2])
        v_costs = int(words[3])
        val = v_proceeds - v_costs
        dc_firms[f_name] = val
        if val > 0:
            l_aver.append(val)
    dc_aver["average_profit"] = round(sum(l_aver) / len(l_aver), 2)
ls_fin.append(dc_firms)
ls_fin.append(dc_aver)
with open("js_5.7.json", "w", encoding="utf-8") as write_f:
    json.dump(ls_fin, write_f, ensure_ascii=False)
