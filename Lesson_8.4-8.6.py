# 8.4
# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 8.5
# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# 8.6
# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Sklad:
    def __init__(self):
        self.lists = {}
        self.give_lists = {}

    def add_to(self, equipment):
        try:
            numb = int(equipment.num)
            self.lists.update({numb: equipment.name})
            print("Получено оборудование: " + equipment.name + " ,серийный номер - " + str(numb))
        except:
            print("Серийный номер не может должен быть целочисленным числовым значением")

        self.lists.update({equipment.num: equipment.name})
        print("Получено оборудование: " + equipment.name + " ,серийный номер - " + str(equipment.num))

    def away_from(self, equipment, other):
        self.give_lists.update({equipment.num: equipment.name})
        print("Забрали: " + equipment.name + ' ,серийный номер - ' + str(equipment.num))
        other.add_to(equipment)

    def list_equipments(self):
        print("Получили: ")
        print(self.lists)
        print("Забрали:")
        print(self.give_lists)


class Equip:
    def __init__(self, name, num):
        self.name = name
        self.num = num


class Printer(Equip):
    def __init__(self, name, num, price):
        Equip.__init__(self, name, num)
        self.price = price

    def __str__(self):
        return "Принтер печатает"


class Scanner(Equip):
    def __init__(self, name, num, volt):
        Equip.__init__(self, name, num)
        self.volt = volt

    def __str__(self):
        return "Сканер сканирует"


class Xerox(Equip):
    def __init__(self, name, num, color):
        Equip.__init__(self, name, num)
        self.color = color

    def __str__(self):
        return "Ксерокс ксерачит"


sk1 = Sklad()
sk2 = Sklad()
pri = Printer("HP", 123456, 18000)
scan = Scanner("Epson", 56789, 4.5)
xe = Xerox("HP", 911, 2)

print(pri)
print(scan)
print(xe)

sk1.add_to(pri)
sk1.add_to(scan)
sk1.add_to(xe)

sk1.away_from(pri, sk2)

sk1.list_equipments()
sk2.list_equipments()
