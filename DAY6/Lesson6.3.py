from random import randint

counter = randint(1, 10)

my_list = [randint(1, 10) for i in range(counter)]

print(f"""Изначальный список: 
{my_list}""")
print("_______________")

if len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
    print("""Количество элементов больше или равно 2, 
добавляем сумму последних двух элементов""")
else:
    my_list.append(0)
    print("""Количество элементов меньше 2, 
в конец добавляем значение 0""")

print(my_list)
