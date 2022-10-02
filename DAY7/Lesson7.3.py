from random import randint

my_list_1 = [randint(1, 100) for i in range(10)]
my_list_2 = [randint(1, 100) for i in range(10)]
print(f"""Изначальные списки: 
{my_list_1}
{my_list_2}""")

my_result = my_list_1[1::2] + my_list_2[0::2]
print("_______________")
print(my_result)
