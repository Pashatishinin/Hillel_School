"""
1. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list по следующему правилу:
Если строка стоит на нечетном месте в my_list, то ее заменить на
перевернутую строку. "qwe" на "ewq".
Если на четном - оставить без изменения.

"""


# Эта функция хранит в себе список, вызывает и возвращает значение функции list_reverced
def list_reverced_start():
    my_list = ["Hello", "Hi", "Danke", "Good Morning", "Achtung"]
    return list_reverced(my_list)


def list_reverced(my_list):
    new_list = my_list.copy()
    for i in range(0, len(my_list), 2):
        new_list[i] = str(my_list[i])[-1::-1]
    return new_list
