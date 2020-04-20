# Класс. Объекты
"""
# Создаем класс Car
class Car:

    # Атрибуты класса
    name = "C200"
    make = "Mersedes"
    model = 2008

    # Методы класса
    def start(self):
        print("Заводим двигатель")

    def stop(self):
        print("Отключаем двигатель")


# Создаем объект класса Car под названием car_a
car_a = Car()
# Создаем объект класса Car под названием car_a
car_b = Car()

# Узнаем тип созданного объекта
print(type(car_b))
# >> <class '__main__.Car'>

# Вызываем метод start() через объект car_a
car_a.start()
# >> Заводим двигатель

# Получаем доступ к атрибуту make модели
print(car_b.make)
# >> 2008
"""

# Класс. Атрибуты класса
"""
# Вывести все атрибуты и методы объекта
print(dir(car_a))
# >> ['__class__',
# >> '__delattr__',
# >> ...
# >>  'start',
# >>  'stop'] 
"""

# Атрибуты класса против атрибутов экземпляров
"""
class Car:

    # Создаем атрибуты класса
    car_count = 0

    # Создаем методы класса
    def start(self, name, make, model):
        print("Двигатель заведен")
        
        # Создаем атрибуты экземпляра
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1

car_a = Car()
car_a.start("Corrola", "Toyota", 2015)
print(car_a.name)
print(car_a.car_count)

car_b = Car()
car_b.start("City", "Honda", 2013)
print(car_b.name)
print(car_b.car_count)
"""

# Методы. Статичные методы
"""
class Car:

    @staticmethod
    def get_class_details():
        print("Это класс Car")


Car.get_class_details()
"""

# Методы. Возврат множественных значений
"""
class Square:

    @staticmethod
    def get_squares(a, b):
        return a * a, b * b


print(Square.get_squares(3, 5))
"""

# Методы. Метод __str__
"""
class Car:

    # Создание методов класса
    def __str__(self):
        return "Car class object"

    def start(self):
        print("Двигатель заведен")


car_b = Car()
print(car_b)
"""

# Конструкторы.
"""
class Car:

    # создание атрибутов класса
    car_count = 0

    # создание методов класса
    def __init__(self):
        Car.car_count += 1
        print(Car.car_count)


car_a = Car()
car_b = Car()
car_c = Car()
"""

# Локальные переменные против глобальных
"""
# Создаем класс Car
class Car:
    def start(self):
        message = "Двигатель заведен"
        return message


car_a = Car()
print(car_a.message)
"""

# Глобальная переменная
"""
# Создаем класс Car
class Car:
    message1 = "Двигатель заведен"

    def start(self):
        message2 = "Автомобиль заведен"
        return message2

car_a = Car()
print(car_a.message1)
print(car_a.message2)
"""

# Модификаторы доступа
"""
class Car:
    def __init__(self):
        print("Двигатель заведен")
        self.name = "corola"        # публичная переменная
        self.__make = "mersedes"    # приватная переменная
        self._model = 1999          # защищенная переменная

car_a = Car()
print(car_a.name)
# print(car_a.__make)
print(car_a._model)
"""

# Наследование
"""
# Создание класса Vehicle
class Vehicle:
    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")


# Создание класса Car, который наследует Vehicle
class Car(Vehicle):
    def car_method(self):
        print("Это метод из дочернего класса Car")


car_a = Car()
car_a.car_method()      # Вызываем метод из дочернего класса
car_a.vehicle_method()  # Вызываем метод из родительского класса
"""

# Множественное наследование
"""
class Vehicle:
    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")

class Car(Vehicle):
    def car_method(self):
        print("Это дочерний метод из класса Car")

class Cycle(Vehicle):
    def cycle_method(self):
        print("Это дочерний метод из класса Cycle")

car_a = Car()
car_a.vehicle_method()
car_b = Cycle()
car_b.vehicle_method()
"""

# Полиморфизм. Перегрузка метода
"""
# Создаем класс Car
class Car:
    def start(self, a, b=None):
        if b is not None:
            print(a + b)
        else:
            print(a)
car_a = Car()
car_a.start(10)
car_a.start(10, 20)
"""

# Полиморфизм. Переопределение метода
"""
# Создаем класс Vehicle
class Vehicle:
    def print_detail(self):
        print("Родительский метод из класса Vehicle")

# Создаем класс Car
class Car(Vehicle):
    def print_detail(self):
        print("Дочерний метод из класса Car")

# Создаем класс Cycle
class Cycle(Vehicle):
    def print_detail(self):
        print("Дочерний метод из класса Cycle")

car_a = Vehicle()
car_a.print_detail()

car_b = Car()
car_b.print_detail()

car_c = Cycle()
car_c.print_detail()
"""

# Инкапсуляция
"""
# Создаем класс Car
class Car:

    # создаем конструктор класса Car
    def __init__(self, model):
        # Инициализация свойств
        self.model = model

    # создаем свойство модели
    @property
    def model(self):
        return self.__model

    # сеттер для создания свойств
    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model

    def getCarModel(self):
        return "Год выпуска модели " + str(self.model)


carA = Car(2005)
print(carA.getCarModel())
"""
