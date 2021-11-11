# 8.1
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, stdat):
        self.stdat = stdat

    @classmethod
    def get_data(cls, stdat):
        lsval = []
        for i in stdat.split():
            if i != "-": lsval.append(i)
        return int(lsval[0]), int(lsval[1]), int(lsval[2])

    @staticmethod
    def valid_data(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 100:
                    return "Данные переданы верно"
                else:
                    return "Неправильный год"
            else:
                return "Неправильный месяц"
        else:
            return "Неправильный день"

    def __str__(self):
        return f"Дата  {Data.get_data(self.stdat)}"


dat1 = Data('11 - 11 - 2021')
print(dat1)
print(Data.valid_data(11, 11, 2023))
print(dat1.valid_data(11, 11, 2011))
print(Data.get_data('11 - 11 - 2011'))
