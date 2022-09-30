a = int(input("Введите число: "))
result_1 = 0

for i in range(2, a + 1):
    if a % i == 0:
        result_1 += i
    else:
        pass

if a == result_1 or a == 1:
    print("______________")
    print(f'{a} - это простое число')
else:
    print("______________")
    print(f'{a} - это не простое число')
