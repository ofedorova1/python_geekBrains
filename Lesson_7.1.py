# 7.1
# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
from copy import deepcopy


class Matrix:
    def __init__(self, mtr):
        self.mtr = mtr

    def __str__(self):
        s = ""
        for i in range(len(self.mtr)):
            s = s + "  ".join(map(str, self.mtr[i])) + "\n"
        return s

    def __add__(self, other):
        if len(self.mtr) != len(other.mtr):
            return None
        res = deepcopy(self.mtr)
        for i in range(len(self.mtr)):
            for k in range(len(self.mtr[i])):
                res[i][k] = self.mtr[i][k] + other.mtr[i][k]
        return Matrix(res)


m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
m = Matrix(m1)
s = Matrix(m2)
print(m)
print(m + s)
