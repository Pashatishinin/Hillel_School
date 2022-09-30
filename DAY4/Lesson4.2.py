N = int(input('Введите число: '))

print("______________")

for i in range(1, N + 1):
    for j in range(1, N):
        if j*j == i:
            print(i, end=" ")
        else:
            pass
