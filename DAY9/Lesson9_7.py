"""
7. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы, которые есть в обеих строках,
но в каждой только по одному разу.
"""


# Эта функция хранит в себе строки, вызывает и возвращает значение функции string_one_symbol
def string_one_symbol_start():
    my_str1 = "Hello, this is my first program"
    my_str2 = "Hi, my name is Pasha!"
    return string_one_symbol(my_str1, my_str2)


def string_one_symbol(my_str1, my_str2):
    new_str = list(set(my_str1) & set(my_str2))
    new_str.pop(new_str.index(" "))
    return new_str
