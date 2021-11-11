# 8.7
# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if self.b + other.b > 0:
            return f"{self.a + other.a} + {self.b + other.b}*i"
        else:
            return f"{self.a + other.a}{self.b + other.b}*i"

    def __mul__(self, other):
        if self.a * other.b + self.b * other.a > 0:
            return f"{self.a * other.a - (self.b * other.b)} + {self.a * other.b + self.b * other.a}*i"
        else:
            return f"{self.a * other.a - (self.b * other.b)}{self.a * other.b + self.b * other.a}*i"

    def __str__(self):
        if self.b > 0:
            return f"{self.a} + {self.b}*i"
        else:
            return f"{self.a}{self.b}*i"


cn1 = ComplexNum(1, 2)
cn2 = ComplexNum(2, -3)
print(cn1)
print(cn2)
print(cn1 + cn2)
print(cn1 * cn2)
