# 5.4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл

from deep_translator import GoogleTranslator

with open("test_file_5.4.txt", "r", encoding="utf-8") as f:
    ls_new = []
    for line in f:
        tmp_ls = line.split()
        translated = GoogleTranslator(source='auto', target='ru').translate(tmp_ls[0])
        line = line.replace(line.split()[0], translated)
        ls_new.append(line)
out_f = open("out_file_5.4.txt", "w", encoding="utf-8")
out_f.writelines(ls_new)
out_f.close()
