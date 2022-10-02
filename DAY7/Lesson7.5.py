from random import randint

my_list = [randint(1, 100) for i in range(10)]

print(f"""Изначальный список: 
{my_list}""")

my_list.append(my_list.pop(0))

print("_______________")
print(my_list)
