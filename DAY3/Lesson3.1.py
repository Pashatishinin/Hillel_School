apples = int(input("Введите количество яблок у вас в корзине: "))
school_kids = int(input("Введите количество школьников: "))

# Услочие если яблок больше чем школьников
if apples > school_kids:
    count = apples // school_kids
    count2 = apples % school_kids
    print("______________")
    print(count2, "Яблок(о) остаеться в корзине")
    print(school_kids, "Школьнику(ам) достаеться по", count, "яблок(у)")

# Условие если школьников больше чем яблок
elif apples < school_kids:
    count = school_kids - apples
    count2 = school_kids % apples
    print("______________")
    print("Яблок в корзине не осталось")
    print(apples, "Школьнику(ам) достаеться по одному яблоку")
    print("Но", count, "Школьник(ов) остался(лись) без яблок")

# Условие если яблок и школьников по ровну
else:
    print("______________")
    print("Яблок в корзине не осталось")
    print(f"{school_kids} Школьнику(ам) досталось по яблоку")
