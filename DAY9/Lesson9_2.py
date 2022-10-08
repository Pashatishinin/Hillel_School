"""
2. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list у которых первый символ - буква "a".
"""


# Эта функция хранит в себе список, вызывает и возвращает значение функции a_begginer
def a_begginer_start():
    my_list = ["Hello", "Hi", "Danke", "Good Morning", "Achtung"]
    return a_begginer(my_list)


def a_begginer(my_list):
    new_list = []
    for i in my_list:
        if str(i).lower().startswith("a"):
            new_list.append(i)
        else:
            pass
    return new_list
