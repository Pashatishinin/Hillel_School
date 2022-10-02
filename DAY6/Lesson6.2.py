from random import randint

my_list = [randint(1, 300) for i in range(20)]
print(f"""Изначальный список: 
{my_list}""")

my_result = []

print("_______________")
print("Список с значениями, которые больше 100")
for i in my_list:
    if i > 100:
        my_result.append(i)

print(my_result)
