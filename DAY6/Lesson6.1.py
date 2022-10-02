from random import randint

my_list = [randint(1, 300) for i in range(10)]
print(f"""Изначальный список: 
{my_list}""")

print("_______________")
print("Значения, которые больше 100")
for i in my_list:
    if i > 100:
        print(i, end=" ")
