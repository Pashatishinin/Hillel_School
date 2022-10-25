import json
import csv


def cenzor(filename, some: list):
    # Открываем файл и пирсваиваем данные с этого файла переменной в виде списка
    with open(filename, 'r') as file:
        data = file.readlines()
    # Проходим циклом по списку
    for j in data:
        # Проходим циклом по списку запрещенных слов
        for i in some:
            # Цикл, пока запрещенное слово есть в строке
            while i in j.lower():
                # Обускаем все симловы в нижний регистр, чтобы можно было найти запрещенное слово в разныъ регистрах
                lower_text = j.lower()
                # Находим индекс первого символа запрещенного слова в строке
                finder = lower_text.find(i)
                # Считаем количество символов в запрещенном слове
                counter = len(i)
                # Создаем замену слову равную по количеству символов
                replace = "*" * counter
                # Находим индекс этой строки в списке
                find_index = data.index(j)
                # Создаем новую строку уже с замененным словом
                j = j[:finder] + replace + j[finder + counter:]
                # Меняем старую строку в списке на новую(культурную) строку
                data[find_index] = j
    # Создаем новую строку
    new_str = ""
    # Проходим циклом по списку, чтобы преобразовать элементы списка в одну строку
    for k in data:
        new_str += k
    # Создаем новый файл и записываем в него новую строку
    with open("new_text2.txt", 'w') as file:
        file.write(new_str)


# Функция создающая JSON файл
def json_creater(filename, some: list):
    # Открываем файл и пирсваиваем данные с этого файла переменной в виде строки
    with open(filename, 'r') as file:
        data = file.read()
    # Создаем словарь с запрещенными словами
    dictionary = dict.fromkeys(some, 0)
    # Обускаем все симловы в нижний регистр, чтобы можно было найти запрещенное слово в разныъ регистрах
    lower_data = data.lower()
    # Проходим циклом по списку запрещенных слов и записываем их количество в сущестующий словарь
    for i in some:
        dictionary[i] = lower_data.count(i)
    # Открываем доступ к файлу
    with open("stat2.txt", "a") as file:
        json.dump({filename: dictionary}, file)

# Функция создающая CSV файл
def csv_creater(filename, some: list):
    # Открываем файл и пирсваиваем данные с этого файла переменной в виде строки
    with open(filename, 'r') as file:
        data = file.read()
    # Создаем словарь с запрещенными словами
    dictionary = dict.fromkeys(some, 0)
    # Обускаем все симловы в нижний регистр, чтобы можно было найти запрещенное слово в разныъ регистрах
    lower_data = data.lower()
    # Проходим циклом по списку запрещенных слов и записываем их количество в сущестующий словарь
    for i in some:
        dictionary[i] = lower_data.count(i)
    # Создаем список
    new_dict = []
    # Проходим циклом по существующему словарю, чтобы преобразовать его в список словарей
    for i in dictionary:
        new_dict.append({"word": i, "count": dictionary.get(i)})
    # Открываем доступ к файлу
    with open("stat2.csv", "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=[filename + ":"])
        writer2 = csv.DictWriter(file, fieldnames=["word", "count"])
        writer.writeheader()
        writer2.writeheader()
        writer2.writerows(new_dict)


def main():
    cenzor(some_text, some_list)
    json_creater(some_text, some_list)
    csv_creater(some_text, some_list)

# Список запрещенных слов
some_list = ['shit', 'fuck', "bitch", "sex", "niggas"]
some_text = "text.txt"
main()
