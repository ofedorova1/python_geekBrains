# 1.3
# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
num = int(input("Введите число:"))
num = str(num)
num_two = num + num
num_three = num_two + num
print(int(num) + int(num_two) + int(num_three))
