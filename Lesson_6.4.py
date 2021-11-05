# 6.4
# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Машинка {self.name} поехала."

    def stop(self):
        return f"Машинка {self.name} остановилась."

    def turn(self, direct):
        if direct == "право":
            return f"Машинка {self.name} повернула направо."
        elif direct == "лево":
            return f"Машинка {self.name} повернула налево."
        else:
            return f"С машиной {self.name} произошла какая-то непонятная ситуация, проверьте переданные данные."

    def show_speed(self):
        return f"Текущая скорость машины {self.name} сейчас {self.speed} км/ч."


class TownCar(Car):

    def show_speed(self):
        print(f"Текущая скорость городской машины {self.name} сейчас {self.speed} км/ч")

        if self.speed > 60:
            return f"Скорость городской машины {self.name} более 60 км/ч, превышение!"
        else:
            return f"Скорость городской машины {self.name} нормальная, продолжайте в том же духе."


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        print(f"Текущая скорость рабочей машины {self.name} сейчас {self.speed} км/ч")

        if self.speed > 40:
            return f"Скорость рабочей машины {self.name} более 40 км/ч, превышение!"
        else:
            return f"Скорость рабочей машины {self.name} нормальная, продолжайте в том же духе."


class PoliceCar(Car):
    pass


car_tw = TownCar(40, "красненькая", "Mazda", False)
print(car_tw.go())
print(car_tw.color)
print(car_tw.show_speed())
print(car_tw.stop())
car_tw_2 = TownCar(85, "синенькая", "Lada", False)
print(car_tw_2.go())
print(car_tw_2.color)
print(car_tw_2.show_speed())
print(car_tw_2.stop())
car_wk = TownCar(40, "беленькая", "Subaru", False)
print(car_wk.go())
print(car_wk.color)
print(car_wk.show_speed())
print(car_wk.stop())
car_wk_2 = TownCar(125, "розовенькая", "Suzuki", False)
print(car_wk_2.go())
print(car_wk_2.color)
print(car_wk_2.show_speed())
print(car_wk_2.turn("право"))
print(car_wk_2.stop())
