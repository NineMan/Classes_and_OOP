"""
Task1. Реализуйте класс Point (точка).

У этого класса должны быть:
- конструктор, принимающий два числа x и y, координаты точки на плоскости;
- атрибуты x и y через которые можно будет получить координаты точки;
- метод dist, который принимает еще один объект класса Point и находит эвклидово расстояние между двумя точками.

Примеры вызова:

p1 = Point(1.5, 1)
p2 = Point(1.5, 2)
p1.dist(p2) == 1

"""

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        return ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5


p1 = Point(0, 0)
p2 = Point(4, 3)
print(p1.dist(p2))
print(p1.dist(p1))
print(p2.dist(p1))
print(p2.dist(p2))


