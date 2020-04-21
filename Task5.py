"""
Task5. BomberMan

Вспомните игру, которую вы делали в восьмом уроке.
Тогда нам приходилось разделять состояние наших игровых объектов,
храня его в словаре, и поведение, раскидывая его по различным функциям.
Теперь вы можете все объединить вместе.

Все игровые объекты имеют много общего.
Все это общее можно вынести в родительский класс GameObject

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True

    def move(self, x, y):
        pass

    def interact(self, other):
        pass

    def logic(self):
        pass
Реализуйте класс Bomb. Унаследуйте его от GameObject.

Вести себя он должен так:

b = Bomb(3, 4)
assert b.x == 3
assert b.y == 4
assert b.alive

b.logic()
assert b.life_time == 2
b.logic()
assert b.life_time == 1
assert b.alive
b.logic()
assert b.life_time == 0
assert not b.alive

"""


class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True

    def move(self, x, y):
        pass

    def interact(self, other):
        pass

    def logic(self):
        pass


class Bomb(GameObject):
    def __init__(self, x, y, life_time=3):
        super().__init__(x, y)              # вызвали метод __init__ родителя
        self.life_time = life_time

    def logic(self):
        self.life_time -= 1
        if not self.life_time:
            self.alive = False
        # self.alive = self.life_time > 0   # альтернативно


b = Bomb(3, 4)
print(b.x)                  # == 3
print(b.y)                  # == 4
print(b.alive)              # == True

b.logic()
print(b.life_time)          # == 2
print(b.alive)

b.logic()
print(b.life_time)          # == 1
print(b.alive)              # == True

b.logic()
print(b.life_time)          # == 0
print(b.alive)              # == False
