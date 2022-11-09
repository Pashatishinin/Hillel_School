# В классе Animal можно ввести данные:
# Название, Вес, Скорость передвижения


class Animal:
    def __init__(self, name, weight, speed):
        self.name = name
        self.weight = weight
        self.speed = speed


# В классе Birds можно ввести данные:
# Название, Вес, Скорость передвижения, Летает или не летает


class Birds(Animal):
    def __init__(self, name, weight, speed, flying):
        # Класс Birds наследствует от класса Animal:
        # Название, Вес, Скорость передвижения
        super().__init__(name, weight, speed)
        self.flying = flying


# В классе Penguin можно ввести данные:
# Название, Вес, Скорость передвижения, Летает или не летает,
# Место происхождения, Размер


class Penguin(Birds):
    def __init__(self, name, weight, speed, origin, size):
        # Класс Penguin наследствует от класса Birds:
        # Название, Вес, Скорость передвижения,
        # данных о полете нет, так как эти животные не летают
        super().__init__(name, weight, speed, None)
        self.origin = origin
        self.size = size

    def say(self):
        print("Pewew")


# В классе Crow можно ввести данные:
# Название, Вес, Скорость передвижения, Летает или не летает,
# Хищник или травоядный


class Crow(Birds):
    def __init__(self, name, weight, speed, flying, predator):
        # Класс Penguin наследствует от класса Birds:
        # Название, Вес, Скорость передвижения, Летает или не летает
        super().__init__(name, weight, speed, flying)
        self.predator = predator

    def say(self):
        print("Carcar")


# В классе Reptile можно ввести данные:
# Название, Вес, Скорость передвижения, Размер, Плавает или не плавает


class Reptile(Animal):
    def __init__(self, name, weight, speed, size, swim):
        # Класс Reptile наследствует от класса Animal:
        # Название, Вес, Скорость передвижения
        super().__init__(name, weight, speed)
        self.size = size
        self.swim = swim


# В классе Snake можно ввести данные:
# Название, Вес, Скорость передвижения, Размер, Плавает или не плавает, Ядовитое или нет


class Snake(Reptile):
    def __init__(self, name, weight, speed, size, swim, poison):
        # Класс Snake наследствует от класса Reptile:
        # Название, Вес, Скорость передвижения, Размер, Плавает или не плавает
        super().__init__(name, weight, speed, size, swim)
        self.poison = poison

    def say(self):
        print("Tststs")


# В классе Crocodile можно ввести данные:
# Название, Вес, Скорость передвижения, Размер, Место происхождения

class Crocodile(Reptile):
    def __init__(self, name, weight, speed, size, origin):
        # Класс Crocodile наследствует от класса Reptile:
        # Название, Вес, Скорость передвижения, Размер,
        # Так как все кракодилы плавают, данные о плаванье опускаются
        super().__init__(name, weight, speed, size, None)
        self.origin = origin

    def say(self):
        print("Arrrrr")


# В классе Mammals можно ввести данные:
# Название, Вес, Скорость передвижения, Размер, Хищники или нет


class Mammals(Animal):
    def __init__(self, name, weight, speed, predator):
        # Класс Mammals наследствует от класса Animal:
        # Название, Вес, Скорость передвижения
        super().__init__(name, weight, speed)
        self.predator = predator


# В классе Bear можно ввести данные:
# Название, Вес, Скорость передвижения, Размер, Хищники или нет,
# Место происхождения, Цвет


class Bear(Mammals):
    def __init__(self, name, weight, speed, predator, origin, color):
        # Класс Bear наследствует от класса Mammals:
        # Название, Вес, Скорость передвижения, Хищник или нет
        super().__init__(name, weight, speed, predator)
        self.origin = origin
        self.color = color

    def say(self):
        print("Rarrr")


# В классе Monkey можно ввести данные:
# Название, Вес, Скорость передвижения,
# Место происхождения, Размер


class Monkey(Mammals):
    def __init__(self, name, weight, speed, origin, size):
        # Класс Bear наследствует от класса Mammals:
        # Название, Вес, Скорость передвижения,
        # Так как обезьяны все не хищники, эти данные опускаются
        super().__init__(name, weight, speed, None)
        self.origin = origin
        self.size = size

    def say(self):
        print("Huhuhaha")
