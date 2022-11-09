import json


class ITMan:
    # Создаем атрибуты класса
    def __init__(self, firstname, lastname, age, email, skills, people_lang, coding_lang):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
        self.email = email
        self.skills = skills
        self.people_lang = people_lang
        self.coding_lang = coding_lang

    # Возвращаем атрибуты экземпляра класса в виде словаря в списке
    def get_list(self):
        return [self.__dict__]


def json_creater(data_list):
    # Записываем список экземпляра класса в JSON
    with open("data_list.txt", "w") as file:
        json.dump(data_list, file)
    # Открываем JSON файл
    with open("data_list.txt", "r") as file:
        total_data = json.load(file)

    # Возвращаем значение JSON файла
    return total_data

# Создаем функцию списка экземпляров класса


def total_list(total_data, append_list):
    total_data = total_data
    append_list = append_list
    # Добавляем в существующий список словаря экзепляра класса словарь нового экземпляра
    total_data.extend(append_list)
    # Перезаписываем JSON файл
    json_creater(total_data)


def main():
    # Присваиваем данные атрибутам экземпляра класса
    obj_1 = ITMan('Ivasik', 'Telesik', 13, 'ivasik-telesik1732@izkrnanog.ua', ['walking', "talking", "coding"],
                  ['Ukrainian', "English"], ['Python', "C++", "lisp"])
    # Присваиваем данные атрибутам экземпляра класса
    obj_2 = ITMan('Petro', 'Ivanov', 18, 'petro-ivanov1234@gmail.com', ['walking', "coding"], ['German', "English"],
                  ['Python', "PHP", "JS"])

    # Присваиваем переменной данные файла JSON
    data_list = json_creater(obj_1.get_list())
    # Запускаем функцию списка экземпляров с двумя данными
    total_list(data_list, obj_2.get_list())


main()
