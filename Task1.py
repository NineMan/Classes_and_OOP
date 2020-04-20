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


