from random import randint

my_list1 = [randint(1, 100) for i in range(10)]
my_list2 = [randint(1, 100) for i in range(10)]

print(f"""Изначальные списки: 
{my_list1}
{my_list2}""")


print(len(set(my_list1)-set(my_list2)))