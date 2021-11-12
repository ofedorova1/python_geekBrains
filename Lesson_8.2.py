# 8.2
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivByNull:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @staticmethod
    def div_by_null(num1, num2):
        try:
            return num1 / num2
        except:
            return "Деление на ноль...не надо так"


nm = DivByNull(50, 10)
print(nm.div_by_null(50, 10))
print(nm.div_by_null(50, 0))
