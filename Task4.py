"""
Task4. Добавим возможность сравнивать объекты класса Circle.

Больше будет тот круг, у которого площадь больше.

sm = Circle(Point(12, 12), 425)
bg = Circle(Point(9, 1), 10293.4)
sm < bg
sm == sm
Для этого вам нужно будет определить несколько специальных методов.
На странице официальной документации языка:
https://docs.python.org/3/reference/datamodel.html#special-method-names
они называются rich comparison methods.

Когда вы их напишите, вы сможете не только сравнивать круги, но и сортировать списки таких объектов:

mid = Circle(Point(0,0), 500.4)
circ_l = [bg, sm, mid]
circ_l.sort()
circ_l[0] is sm and circ_l[1] is mid and circ_l[2] is bg

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
        return self.radius ** 2 * 3.14

    def do_intersect(self, circle):
        r_center = self.center.dist(circle.center)
        r_radius = self.radius + circle.radius
        return r_center <= r_radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius


sm = Circle(Point(12, 12), 425)
bg = Circle(Point(9, 1), 10293.4)
mid = Circle(Point(0, 0), 500.4)

print(sm > bg)
print(sm > sm)

circ_l = [bg, sm, mid]
circ_l.sort()
print(circ_l[0] == sm)
print(circ_l[1] == mid)
print(circ_l[2] == bg)

# circ_l[0] is sm and circ_l[1] is mid and circ_l[2] is bg
