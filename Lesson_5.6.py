# 5.6
# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
"""Красивый читерский способ"""
import re

with open("test_file_5.6.txt", "r", encoding="utf-8") as f:
    fin_dict = {}
    for line in f:
        les_name = line.split()[0].replace(":", "")
        les_hours = sum(map(int, re.findall("\d+", line)))
        fin_dict[les_name] = les_hours
print(fin_dict)

"""Долгий и мучительный способ"""
with open("test_file_5.6.txt", "r", encoding="utf-8") as f:
    sec_dict = {}
    for line in f:
        l_nam = line.split()[0].replace(":", "")
        ls_h = 0
        l = len(line)
        integ = []
        i = 0
        while i < l:
            s_int = ''
            a = line[i]
            while '0' <= a <= '9':
                s_int += a
                i += 1
                if i < l:
                    a = line[i]
                else:
                    break
            i += 1
            if s_int != '':
                integ.append(int(s_int))
            ls_h = sum(integ)
            sec_dict[l_nam] = ls_h
print(sec_dict)
