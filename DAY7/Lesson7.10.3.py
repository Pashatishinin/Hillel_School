my_list = list(input("Введите элементы строки: ").split())

for i in my_list:
    if i.isdigit():
        my_list.pop(my_list.index(i))

print("_______________")
print(my_list)

