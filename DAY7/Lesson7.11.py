my_str = input("Введите строку: ")

my_list = []
for i in my_str:
    if my_str.count(i) > 1:
        continue
    else:
        my_list.append(i)

print("_______________")
print(my_list)
