def cenzor(filename, some):
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
    with open("new_text.txt", 'w') as file:
        file.write(new_str)


# список запрещенных слов
some_list1 = ['shit', 'fuck', "bitch", "sex", "niggas"]

cenzor('text.txt', some_list1)
