from random import randint

my_list = [randint(1,10)for i in range(10)]
print(f"""Изначальный список: 
{my_list}""")

result = []
for j in my_list:
    k = my_list.index(j)
    if my_list[0] is j or my_list[-1] is j:
        pass
    elif j > (my_list[k-1]+my_list[k+1]):
        result.append(j)

print("_______________")
print(len(result))
