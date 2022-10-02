from random import randint

my_list = [randint(1, 100) for i in range(10)]

k = randint(1, 9)

print(f"""Изначальный список: 
{my_list}""")
print(f"Индекс 'к' равен [{k}]")

print("_______________")
C = input("Введите значение С: ")

print("_______________")

my_list[k:-1] = list([C]) + my_list[k:-1]
print(my_list)
