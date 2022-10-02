my_list = [1, 2, 3, '11', "22", 33]

print(f"""Изначальный список: 
{my_list}""")

my_result = []
for i in my_list:
    if isinstance(i, str):
        my_result.append(i)

print("_______________")
print(my_result)
