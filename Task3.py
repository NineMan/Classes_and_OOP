"""
Task3. Доработаем ваш класс Circle. 

Добавьте ему метод do_intersect, 
который будет принимать другой объект класса Circle 
и возвращать True или False в зависимости от того, 
пересекаются круги или нет.

Весь остальной код класса вы можете скопировать из решения предыдущей задачи.

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
        p1 = self.center
        p2 = circle.center
        r_center = p1.dist(p2)
        r_radius = self.radius + circle.radius
        if r_center <= r_radius:
            return True
        else:
            return False


circ1 = Circle(Point(0, 0), 2)
circ2 = Circle(Point(0, 4), 1)
print(circ1.do_intersect(circ2))
