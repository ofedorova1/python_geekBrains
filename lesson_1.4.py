# 1.4
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число число:"))
maxNumber = 0
while number >= 10:
    if maxNumber < number % 10:
        maxNumber = number % 10
    number = number // 10
if number < maxNumber:
    print(maxNumber)
else:
    print(number)
