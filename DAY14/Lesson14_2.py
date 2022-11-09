# В классе Animal можно ввести данные:
# Имя, Тип(Домашнее, Дикое), Голос - который издает животное


class Animal:
    def __init__(self, name, type_animal, voice):
        self.name = name
        self.type_animal = type_animal
        self.voice = voice

    def say(self):
        print(f"""
Животное {self.name} издает звук {self.voice}
""")


# В классе Birds можно ввести данные:
# Имя, Тип(Домашнее, Дикое), Голос - который издает животное, Летает или не летает


class Birds(Animal):
    def __init__(self, name, type_animal, voice, flying):
        # Класс Birds наследствует от класса Animal:
        # Имя, Тип(Домашнее, Дикое), Голос - который издает животное
        super().__init__(name, type_animal, voice)
        self.flying = flying


# В классе Penguin можно ввести данные:
# Имя, Тип(Домашнее, Дикое), Голос - который издает животное, Летает или не летает,
# Место происхождения, Размер


class Penguin(Birds):
    def __init__(self, name, type_animal, voice, origin, size):
        # Класс Penguin наследствует от класса Birds:
        # Имя, Тип(Домашнее, Дикое), Голос - который издает животное,
        # данных о полете нет, так как эти животные не летают
        super().__init__(name, type_animal, voice, None)
        self.origin = origin
        self.size = size


# В классе Crow можно ввести данные:
# Имя, Тип(Домашнее, Дикое), Голос - который издает животное, Летает или не летает,
# Хищник или травоядный


class Crow(Birds):
    def __init__(self, name, type_animal, voice, flying, predator):
        # Класс Penguin наследствует от класса Birds:
        # Имя, Тип(Домашнее, Дикое), Голос - который издает животное, Летает или не летает
        super().__init__(name, type_animal, voice, flying)
        self.predator = predator


# В классе Reptile можно ввести данные:
# Имя, Тип(Домашнее, Дикое), Голос - который издает животное, Размер, Плавает или не плавает


class Reptile(Animal):
    def __init__(self, name, type_animal, voice, size, swim):
        # Класс Reptile наследствует от класса Animal:
        # Имя, Тип(Домашнее, Дикое), Голос - который издает животное
        super().__init__(name, type_animal, voice)
        self.size = size
        self.swim = swim


# В классе Snake можно ввести данные:
# Имя, Тип(Домашнее, Дикое), Голос - который издает животное, Размер, Плавает или не плавает, Ядовитое или нет


class Snake(Reptile):
    def __init__(self, name, type_animal, voice, size, swim, poison):
        # Класс Snake наследствует от класса Reptile:
        # Имя, Тип(Домашнее, Дикое), Голос - который издает животное, Размер, Плавает или не плавает
        super().__init__(name, type_animal, voice, size, swim)
        self.poison = poison


# В классе Crocodile можно ввести данные:
# Имя, Тип(Домашнее, Дикое), Голос - который издает животное, Размер, Место происхождения

class Crocodile(Reptile):
    def __init__(self, name, type_animal, voice, size, origin):
        # Класс Crocodile наследствует от класса Reptile:
        # Имя, Тип(Домашнее, Дикое), Голос - который издает животное, Размер,
        # Так как все кракодилы плавают, данные о плаванье опускаются
        super().__init__(name, type_animal, voice, size, None)
        self.origin = origin


# В классе Mammals можно ввести данные:
# Имя, Тип(Домашнее, Дикое), Голос - который издает животное, Размер, Хищники или нет


class Mammals(Animal):
    def __init__(self, name, type_animal, voice, predator):
        # Класс Mammals наследствует от класса Animal:
        # Имя, Тип(Домашнее, Дикое), Голос - который издает животное
        super().__init__(name, type_animal, voice)
        self.predator = predator


# В классе Bear можно ввести данные:
# Имя, Тип(Домашнее, Дикое), Голос - который издает животное, Размер, Хищники или нет,
# Место происхождения, Цвет


class Bear(Mammals):
    def __init__(self, name, type_animal, voice, predator, origin, color):
        # Класс Bear наследствует от класса Mammals:
        # Имя, Тип(Домашнее, Дикое), Голос - который издает животное, Хищник или нет
        super().__init__(name, type_animal, voice, predator)
        self.origin = origin
        self.color = color


# В классе Monkey можно ввести данные:
# Имя, Тип(Домашнее, Дикое), Голос - который издает животное, Размер,
# Место происхождения, Размер


class Monkey(Mammals):
    def __init__(self, name, type_animal, voice, origin, size):
        # Класс Bear наследствует от класса Mammals:
        # Имя, Тип(Домашнее, Дикое), Голос - который издает животное,
        # Так как обезьяны все не хищники, эти данные опускаются
        super().__init__(name, type_animal, voice, None)
        self.origin = origin
        self.size = size
