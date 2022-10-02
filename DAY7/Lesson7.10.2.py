my_list = list(input("Введите элементы строки: ").split())

my_result = []
for i in my_list:
    if i.isdigit():
        continue
    else:
        my_result.append(i)

print("_______________")
print(my_result)
