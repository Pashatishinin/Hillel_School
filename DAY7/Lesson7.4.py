from random import randint

my_list = [randint(1, 100) for i in range(10)]

print(f"""Изначальный список: 
{my_list}""")

new_list = my_list[1:10] + list([my_list[0]])
print("_______________")
print(new_list)
