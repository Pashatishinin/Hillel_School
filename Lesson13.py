import os


# Создаем класс
class DirWorker:
    """
    1. Инициализация класса с одним параметром - имя директории.
    """

    # Создание параметра текущей директории
    def __init__(self, dir_name: str):
        self.dirname = dir_name

    """
    2. Написать метод класса, который создает атрибут класса в ввиде словаря
    {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
    Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))
    {'filenames': [файл1, файл2, файл7], 'dirnames': [папка1, папка2]}
    """

    # Создаем метод, который создаем словарь из файлов и папок
    @staticmethod
    def dict_creator(dir_name=None):
        # Записываем все элементы директории в переменную
        data = os.listdir(dir_name)

        # Создаем словарь с двумя ключами
        dictionary = dict.fromkeys(['filenames', 'dirnames'])
        # Cоздаем два пустых списка
        dirnames = []
        filenames = []
        # Проходим циклом по списку элементов директории
        for i in data:
            # Исключить эти специальные файлы
            if ".fleet" in i or ".git" in i or ".idea" in i or "__pycache__" in i:
                pass
            # Если это не файл, поместить его в список папок
            elif "." not in i:
                dirnames.append(i)
            # Остаток поместить в список файлов
            else:
                filenames.append(i)
        # Присвоить ключу "dirnames" значения списка dirnames
        dictionary['dirnames'] = dirnames
        # Присвоить ключу "filenames" значения списка filenames
        dictionary['filenames'] = filenames
        # Возвращаем словарь
        return dictionary

    """
    2. Написать метод класса, которая получает булевое значение (True/False).
    Функция возвращает тот же словарь, но с отсортированными именами файлов и папок 
    в соответствующих списках.
    Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.
    """

    # Создаем метод сортировки
    @staticmethod
    def dictionary_sorter(reverse=None):
        # Если reverse существует, то сортируем список по алфавиту
        if reverse:
            # Создаем переменную со значениями ключа filenames
            sorter_filenames = data_dictionary['filenames']
            # Cортируем значения переменной
            sorter_filenames.sort()
            # Создаем переменную со значениями ключа dirnames
            sorter_dirnames = data_dictionary['dirnames']
            # Cортируем значения переменной
            sorter_dirnames.sort()
        # Если reverse не существует, то сортируем список по в обратном напровлении
        else:
            # Создаем переменную со значениями ключа filenames
            sorter_filenames = data_dictionary['filenames']
            # Cортируем значения переменной
            sorter_filenames.sort(reverse=True)
            # Создаем переменную со значениями ключа dirnames
            sorter_dirnames = data_dictionary['dirnames']
            # Cортируем значения переменной
            sorter_dirnames.sort(reverse=True)
        # Возвращаем новый словарь
        return data_dictionary

    """
    3. Написать метод класса, которая получает строку, которая может быть
    или именем файла, или именем папки. (В имени файла должна быть точка).
    В зависимости от того, что функция получила (имя файла или имя папки) - записать его
    в соответствующий список и вернуть обновленный словарь.
    """

    # Создаем метод добавления нового элемента в словарь
    @staticmethod
    def new_file_method(name):
        # Если это файл, добавить в список файлов в словаре
        if "." in name:
            new_file = data_dictionary['filenames']
            new_file.append(name)
            data_dictionary['filenames'] = new_file
        # Если нет, добавить в список папок в словаре
        else:
            new_dir = data_dictionary['dirnames']
            new_dir.append(name)
            data_dictionary['dirnames'] = new_dir
        # Возвращаем новый словарь
        return data_dictionary

    """
    4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
    Написать метод класса, которая получает имя директори и словарь по примеру из задания 1.
    Функция проверяет соответствие полученного словаря и реальной файловой системы в полученной папке и,
    если надо, создает нужные папки и пустые файлы, в соответствии со структурой словаря.
    Пример:
    создали на основании данных в папке -> {'filenames': [файл1, файл2, файл7], 'dirnames': [папка1, папка2]}
    передали в метод -> {'filenames': [файл1, файл7, файл13], 'dirnames': [папка11, папка2]}
    в результате необходимо создать файл13 и папка11
    """

    # Cоздаем метод сравнения словарей
    @staticmethod
    def file_comp(second_dict, dir_name=None):
        data = DirWorker.dict_creator(dir_name)
        data2 = second_dict
        # Присваиваем списку new_dirnames значения ключа "dirnames"
        new_dirnames = data['dirnames']
        # Присваиваем списку new_filenames значения ключа "filenames"
        new_filenames = data['filenames']

        # Сравниваем два списка при помощи функций множеств, и разницу присваиваем filenames
        filenames = set(data2['filenames']).difference(set(data['filenames']))
        # Сравниваем два списка при помощи функций множеств, и разницу присваиваем dirnames
        dirnames = set(data2['dirnames']).difference(set(data['dirnames']))
        # Проходим циклом по dirnames, создаем папку и добавляем к списку new_dirnames
        for i in dirnames:
            os.makedirs(i)
            new_dirnames.append(i)
        # Проходим циклом по filenames, создаем файл и добавляем к списку new_filenames
        for j in filenames:
            with open(j, 'w') as file:
                file.write("")
            new_filenames.append(j)
        # Обнавляем значения ключей словаря
        data['dirnames'] = new_dirnames
        data['filenames'] = new_filenames


# Присваемваем переменной имя текущей директории
path_directory = os.getcwd()

# Присваиваем имя текущей директории экземпляру класса
dirname = DirWorker(path_directory)

# Присваиваем переменной значение функции
data_dictionary = dirname.dict_creator()

# Булевое значение сортировки
sort_or_reverse = True

# Присваиваем переменной значение функции
new_dictionary = dirname.dictionary_sorter(sort_or_reverse)

# Создаем переменную с новый элементом
new_name = "text.py"

# Присваиваем переменной значение функции
renew_dictionary = dirname.new_file_method(new_name)

# Второй словарь файлов и папок
second_dictionary = {'filenames': ["файл1.txt", "файл2.txt", "файл7.txt"], 'dirnames': ["папка1", "папка2"]}

# Присваиваем переменной значение функции
dirname.file_comp(second_dictionary)
