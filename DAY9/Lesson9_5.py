"""5. Написать функцию которой передается один параметр - строка my_str.
Функция возвращает новый список в котором содержаться те символы из my_str,
которые встречаются в строке только один раз.
"""


# Эта функция хранит в себе строку, вызывает и возвращает значение функции one_count_symbol
def one_count_symbol_start():
    my_str = "Hello, this is my first program"
    return one_count_symbol(my_str)


def one_count_symbol(my_str):
    my_str = my_str.split(" ")
    new_str = []
    for i in my_str:
        for j in i:
            if j not in new_str:
                new_str.append(j)
            else:
                new_str.remove(j)
    return new_str
