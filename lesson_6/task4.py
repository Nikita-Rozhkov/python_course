"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} стартовал'

    def stop(self):
        return f'{self.name} остановился'

    def turn_right(self):
        return f'{self.name} повернул направо'

    def turn_left(self):
        return f'{self.name} повернул налево'

    def show_speed(self):
        return f'Скорость {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость городского автомобиля{self.name} {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышена'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость рабочего автомобиля {self.name} {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышена'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - полицейский автомобиль'
        else:
            return f'{self.name} не полицейский автомобиль'


ford = SportCar(80, 'синий', 'Ford', False)
bmw = TownCar(50, 'жёлтый', 'BMW', False)
audi = WorkCar(90, 'чёрный', 'Audi', True)
volvo = PoliceCar(110, 'белый',  'Volvo', True)
print(audi.turn_left())
print(bmw.turn_right(), ford.stop())
print(audi.go(), audi.show_speed())
print(audi.name, audi.color)
print(ford.name, ford.is_police)
print(volvo.name, volvo.is_police)
print(bmw.show_speed())
print(volvo.show_speed())
print(volvo.police())
print(ford.show_speed())