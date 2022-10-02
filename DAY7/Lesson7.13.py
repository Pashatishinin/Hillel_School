my_str1 = list(input("Введите первую строку: "))
my_str2 = list(input("Введите вторую строку: "))

for i in my_str1:
    if my_str1.count(i) > 1 or i == " ":
        while i in my_str1:
            my_str1.remove(i)

for j in my_str2:
    if my_str2.count(j) > 1 or j == " ":
        while j in my_str2:
            my_str2.remove(j)

my_list = list(set(my_str1) & set(my_str2))

print("_______________")
print(my_list)
