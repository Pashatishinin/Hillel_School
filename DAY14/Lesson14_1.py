# В классе Transport можно ввести данные: гос. номер, количество колес, мощность двигателя, скорость


class Transport:
    def __init__(self, gos_number, wheels, power_engine, speed):
        self.gos_number = gos_number
        self.wheels = wheels
        self.power_engine = power_engine
        self.speed = speed


# В классе Bicycle можно ввести данные:
# гос. номер, мощность двигателя, скорость, тип транспорта(фэтбайк, BMX, горный, детский)


class Bicycle(Transport):
    def __init__(self, gos_number, power_engine, speed, transport_type):
        # Класс Bicycle наследствует от класса Transport гос. номер, мощность двигателя, скорость
        # Количество колес ставиться константой (2)
        super().__init__(gos_number, 2, power_engine, speed)
        self.transport_type = transport_type


# В классе Auto можно ввести данные:
# гос. номер, мощность двигателя, скорость, тип транспорта(Хэтчбэк, Лимузин, Внедорожник, Купе, Кабриолет...),
# тип двигателя(газ, бензин, электро)


class Auto(Transport):
    def __init__(self, gos_number, power_engine, speed, transport_type, type_engine):
        # Класс Auto наследствует от класса Transport гос. номер, мощность двигателя, скорость
        # Количество колес ставиться константой (4)
        super().__init__(gos_number, 4, power_engine, speed)
        self.transport_type = transport_type
        self.type_engine = type_engine


# В классе Bus можно ввести данные:
# гос. номер, количество колес, мощность двигателя, скорость, размер автобуса,
# предназначение(Маршутный, Школьный, Рабочий)


class Bus(Transport):
    def __init__(self, gos_number, wheels, power_engine, speed, size, purpose):
        # Класс Bus наследствует от класса Transport гос. номер, количество колес, мощность двигателя, скорость
        super().__init__(gos_number, wheels, power_engine, speed)
        self.size = size
        self.purpose = purpose


# В классе Bus можно ввести данные:
# гос. номер, количество колес, мощность двигателя, скорость, размер грузовика,
# предназначение(Бензовоз, Товарный, Строительный), размер грузоподьемности


class Truck(Bus):
    def __init__(self, gos_number, wheels, power_engine, speed, size, purpose, weight):
        # Класс Truck наследствует от класса Bus гос. номер, количество колес, мощность двигателя,
        # скорость, размер, предназначение
        super().__init__(gos_number, wheels, power_engine, speed, size, purpose)
        self.weight = weight


# В классе Moto можно ввести данные:
# гос. номер, мощность двигателя, скорость, тип транспорта(Scooter, Cafe Racer, Cruiser, Classic...),
# тип двигателя(газ, бензин, электро)


class Moto(Bicycle):
    def __init__(self, gos_number, power_engine, speed, transport_type, type_engine):
        # Класс Moto наследствует от класса Bicycle гос. номер, мощность двигателя, скорость и тип транспорта
        super().__init__(gos_number, power_engine, speed, transport_type)
        self.type_engine = type_engine
