from random import randint

my_list = [randint(1, 100) for i in range(10)]
print(f"""Изначальный список: 
{my_list}""")

k = randint(1, 9)
print("_______________")
print(f"""Индекс 'к' равен [{k}] 
c значением  [{my_list[k]}]""")

my_list[k:-1] = my_list[k + 1:-1]
my_list.pop()
print("_______________")
print(my_list)
