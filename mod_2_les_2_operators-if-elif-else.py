# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else"

print('Введите три целых числа ниже, одно за другим: ')
first = input()
second = input()
third = input()
if first == second and third == first :
    print(3)
elif first == second or third == first:
    print(2)
else:
    print(0)
