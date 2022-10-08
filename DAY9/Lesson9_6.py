"""
6. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы,
которые есть в обеих строках хотя бы раз.
"""


# Эта функция хранит в себе строки, вызывает и возвращает значение функции string_count_symbol
def string_count_symbol_start():
    my_str1 = "Hello, this is my first program"
    my_str2 = "Hi, my name is Pasha!"
    return string_count_symbol(my_str1, my_str2)


def string_count_symbol(my_str1, my_str2):
    new_str = list(set(my_str1).union(set(my_str2)))
    new_str.pop(new_str.index(" "))
    return new_str
