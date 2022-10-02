my_list = input("Введите элементы строки: ").split()
total = 0
for i in my_list:
    if i.isdigit():
        total += int(i)
    else:
        continue
print("_______________")
print(f"Сумма всех чисел в этой строке равна - {total}")
