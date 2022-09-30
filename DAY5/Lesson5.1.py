inform = """
------------------------------------------------
ВНИМАНИЕ! Данная фигура имеет острые углы сверху и снизу. И не может иметь высоту с четным значением.
Поэтому при вводе четного значение, программа будет автоматически округлять значение на единицу в большую сторону
------------------------------------------------
"""

# Треугольник слева
height1 = int(input(f"{inform}Введите ввысоту треугольника слева: "))//2+1
weight1 = height1

for h in range(height1):
    for w in range(h + 1):
        print('*', end=" ")
    print()
for h in range(height1, 0, -1):
    for w in range(h - 1):
        print('*', end=" ")
    print()

# Треугольник снизу
height2 = int(input("Введите ввысоту треугольника снизу: "))
weight2 = height2 * 2 - 1

for h in range(height2):
    for w in range(weight2):
        if h + w <= height2 - 2:
            print(' ', end=" ")
            continue
        if w - h <= height2 - 1:
            print('*', end=" ")
            continue
        print(' ', end=" ")
    print()

# Треугольник справа
height3 = int(input(f"{inform}Введите ввысоту треугольника справа: "))//2+1
weight3 = height3

for h in range(height3):
    for w in range(weight3):
        if h + w >= weight3:
            print('*', end=" ")
            continue
        print(' ', end=" ")
    print()
for h in range(height3, 0, -1):
    for w in range(weight3):
        if h + w >= weight3:
            print('*', end=" ")
            continue
        print(' ', end=" ")
    print()

# Треугольник сверху
height4 = int(input("Введите ввысоту треугольника сверху: "))
weight4 = height4 * 2 - 1

for h in range(height4):
    for w in range(weight4):
        if w < h:
            print(' ', end=" ")
            continue
        if w + h >= weight4:
            print(' ', end=" ")
            continue
        print('*', end=" ")
    print()
