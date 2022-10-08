"""
3. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list в которых есть символ - буква "a" на любом месте.
"""


# Эта функция хранит в себе список, вызывает и возвращает значение функции a_searching
def a_searching_start():
    my_list = ["Hello", "Hi", "Danke", "Good Morning", "Achtung"]
    return a_searching(my_list)


def a_searching(my_list):
    new_list = []
    for i in my_list:
        if "a" in str(i).lower():
            new_list.append(i)
    return new_list
