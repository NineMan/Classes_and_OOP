"""
Task2. Напишите класс Circle, представляющий круг.

У этого класса должны быть:

- конструктор принимающий объект класса Point, точку центра круга, и число, радиус круга;
- атрибуты center и radius, возвращающие центр и радиус круга соответственно;
- метод square, который возвращает площадь круга.
Класс Point вы можете использовать в своем коде без объявления (т.е. вам не нужно его писать).

circ = Circle(Point(0, 3), 4)
circ.radius == 4
circ.center.x == 0

Circle(Point(0, 0), 0).square() == 0
Вычисления будут проверятся с точностью до второго знака после запятой.
Можете не использовать слишком точные приближения числа \piπ.

"""


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        return ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5


class Circle:
    def __init__(self, point, radius):
        self.center = point
        self.radius = radius

    def square(self):
        return self.radius * self.radius * 3.14


circ = Circle(Point(0, 3), 4)
print(circ.radius)                          # == 4
print(circ.center.x)                        # == 0
print(Circle(Point(0, 0), 1).square())      # == 0


# Circle(Point(120, -324), 43).square(), 3.14 * 43 * 43
print(Circle(Point(120, -324), 43).square())
print(3.14 * 43 * 43)
