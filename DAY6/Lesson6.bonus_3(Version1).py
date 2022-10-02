from random import randint

my_list1 = [randint(1, 100) for i in range(10)]
my_list2 = [randint(1, 100) for i in range(10)]

print(f"""Изначальные списки: 
{my_list1}
{my_list2}""")
counter = []
for i in my_list1:
    count = my_list1.count(i)
    if count == 1:
        counter.append(count)

print("_______________")
print(f"""Количество уникальных элементов в списке 
{my_list1} - {len(counter)}""")

counter = []
for i in my_list2:
    count = my_list2.count(i)
    if count == 1:
        counter.append(count)
print(f"""Количество уникальных элементов в списке
{my_list2} - {len(counter)}""")
