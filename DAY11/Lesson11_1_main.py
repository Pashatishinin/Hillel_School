import csv
import json
import Lesson11_2_cenzor

# Список запрещенных слов
some_list = ['shit', 'fuck', "bitch", "sex", "niggas"]


# Функция создающая JSON файл
def json_creater():
    # Открываем доступ к файлу
    with open("stat.txt", "a") as file:
        json.dump(Lesson11_2_cenzor.cenzor('text.txt', some_list), file)


# Функция создающая CSV файл
def csv_creater():
    # Создаем список
    new_dict = []
    # Проходим циклом по существующему словарю, чтобы преобразовать его в список словарей
    for i in Lesson11_2_cenzor.cenzor('text.txt', some_list):
        new_dict.append({"word": i, "count": Lesson11_2_cenzor.cenzor('text.txt', some_list).get(i)})

    # Открываем доступ к файлу
    with open("stat.csv", "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["word", "count"])
        writer.writeheader()
        writer.writerows(new_dict)


json_creater()
csv_creater()
