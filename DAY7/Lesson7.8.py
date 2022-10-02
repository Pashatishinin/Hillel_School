my_str = input("Введите строку: ")

if len(my_str) % 2 != 0:
    my_str += "_"

counter = 2
total = []
while len(my_str) >= counter:
    total.append(my_str[counter - 2:counter])
    counter += 2

print("_______________")
print(total)
