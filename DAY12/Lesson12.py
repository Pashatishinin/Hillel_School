import json


class ITMan:

    def __init__(self, firstname, lastname, age, email, skills, people_lang, coding_lang):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
        self.email = email
        self.skills = skills
        self.people_lang = people_lang
        self.coding_lang = coding_lang

    def get_list(self):
        return [self.__dict__]


def json_creater(data_list):
    with open("data_list.txt", "w") as file:
        json.dump(data_list, file)

    with open("data_list.txt", "r") as file:
        total_data = json.load(file)

    return total_data


def total_list(total_data, append_list):
    total_data = total_data
    append_list = append_list
    total_data.extend(append_list)

    json_creater(total_data)


def main():
    obj_1 = ITMan('Ivasik', 'Telesik', 13, 'ivasik-telesik1732@izkrnanog.ua', ['walking', "talking", "coding"],
                  ['Ukrainian', "English"], ['Python', "C++", "lisp"])
    obj_2 = ITMan('Petro', 'Ivanov', 18, 'petro-ivanov1234@gmail.com', ['walking', "coding"], ['German', "English"],
                  ['Python', "PHP", "JS"])
    data_list = json_creater(obj_1.get_list())
    total_list(data_list, obj_2.get_list())


main()
