"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. А
трибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
 Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

class Road:
    _length = None
    _width = None
    weigth = None
    thickness = None
    def __init__(self, length, width):
        self.length =length
        self.width = width

    def mass(self):
        self.weigth = 25
        self.thickness = 0.05
        mass = self.length * self.width * self.weigth * self.thickness / 1000
        print(mass)

road = Road(5000, 20)
road.mass()