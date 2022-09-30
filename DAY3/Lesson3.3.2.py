number = int(input("Введите любое трехзначное число: "))
total = 0

while number > 0:
    count = number % 10
    number //= 10
    total *= 10
    total += count

print("______________")
print(f'Перевернутое число будет: {total}')
