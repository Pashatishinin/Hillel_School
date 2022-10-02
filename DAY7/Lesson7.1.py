from random import randint

a = randint(1,10000000000)
b = str(a)
result = ""
for i in b:
    if i == "0":
        result += i
print("_______________")
print(f"В числе {a} - {len(result)} нуля(ей)")


