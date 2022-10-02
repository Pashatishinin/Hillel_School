my_str = input("Введите строку: ")

l_limit = input("Введите левый символ строки: ")
r_limit = input("Введите правый символ строки: ")

sub_str = my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]
print("_______________")
print(sub_str)
