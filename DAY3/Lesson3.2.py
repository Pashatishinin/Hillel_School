class_a = int(input('Введите количество учащихся в классе А: '))
class_b = int(input('Введите количество учащихся в классе B: '))
class_c = int(input('Введите количество учащихся в классе C: '))

count_tables_a = class_a // 2
count_one_more_table_a = class_a % 2
print("______________")
print(f'Для класса А нужно закупить {count_tables_a+count_one_more_table_a} парт')

count_tables_b = class_b // 2
count_one_more_table_b = class_b % 2
print(f'Для класса B нужно закупить {count_tables_b+count_one_more_table_b} парт')

count_tables_c = class_c // 2
count_one_more_table_c = class_c % 2
print(f'Для класса C нужно закупить {count_tables_c+count_one_more_table_c} парт')

# Если количество учащихся нечетное в классах, то можно сэкономить на покупке парт.
# Так как за партой сидит только один человек

print("______________")
if count_one_more_table_c != 0 and count_tables_b != 0:
    print('Но, можно с класса В перевести одного учащегося в класс С и купить на одну парту меньше')
elif count_one_more_table_a != 0 and count_tables_b != 0:
    print('Но, можно с класса A перевести одного учащегося в класс B и купить на одну парту меньше')
elif count_one_more_table_a != 0 and count_tables_c != 0:
    print('Но, можно с класса A перевести одного учащегося в класс C и купить на одну парту меньше')
else:
    pass
