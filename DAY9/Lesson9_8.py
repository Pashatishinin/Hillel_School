"""
8. Даны списки names и domains (создать самостоятельно).
Написать функцию для генерирования e-mail в формате:
фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
Строку и число генерировать случайным образом.
"""
from random import randint


# Эта функция хранит в себе списки, вызывает и возвращает значение функции random_name_mail
def random_name_mail_start():
    names = ["John", "Mark", "Pasha", "Timon", "Pumba", "Simba", "Anton"]
    domains = ["com", "net", "org", "com.ua"]
    return random_name_mail(names, domains)


# Эта функция возвращает случайную строку.
def random_counter():
    i = 0
    text = ""
    while i <= 5:
        text += chr(randint(97, 122))
        i += 1
    return text


def random_name_mail(names, domains):
    n = randint(0, len(names) - 1)
    d = randint(0, len(domains) - 1)
    number = randint(100, 999)
    return f"{names[n]}{number}@{random_counter()}.{domains[d]}"
