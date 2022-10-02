from random import randint

a = randint(1, 10000000000)
b = str(a)[-1::-1]
result = ""
for i in b:
    if i == "0":
        result += i
    elif i != "0":
        break
print("_______________")
print(f"В конце числа {a} - {len(result)} нуля(ей)")
