# 1.6
# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
first = float(input("Введите количество километров за первый день:"))
allK = float(input("Введите требуемое количество километров:"))
day = 1
while first <= allK:
    day = day + 1
    first = first + 0.1 * first
print("Спортсмен достигнет требуемого результата на {0}-ый день".format(day))
