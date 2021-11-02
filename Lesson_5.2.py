# 5.2
# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open("test_file_5.1.txt", "r", encoding="utf-8") as f:
    count = 0
    my_list = []
    for line in f:
        count += 1
        my_list.append(len(line.split()))
print("Количество строк: " + str(count))
print("Количество слов по строкам:")
for i in my_list:
    print(i)
