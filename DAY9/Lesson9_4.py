"""
4. Написать функцию которой передается один параметр - список строк my_list в
котором могут быть как строки (type str) так и целые числа (type int).
Функция возвращает новый список в котором содержаться только строки из my_list.
"""


# Эта функция хранит в себе список, вызывает и возвращает значение функции list_watcher
def list_wathcer_start():
    my_list = ["Hello", 44, "Hi", 27, 34, 13, "Good Morning", "Achtung"]
    return list_watcher(my_list)


def list_watcher(my_list):
    new_list = []
    for i in my_list:
        if type(i) is str:
            new_list.append(i)
    return new_list
