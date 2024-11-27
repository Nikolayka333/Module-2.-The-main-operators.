# Домашняя работа по уроку "Стиль кода. Цикл While.

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
initial_value = 0
while initial_value < len(my_list):
    print(my_list[initial_value])
    initial_value += 1
    if  my_list[initial_value] >= 0:
        continue
    else:
        break
