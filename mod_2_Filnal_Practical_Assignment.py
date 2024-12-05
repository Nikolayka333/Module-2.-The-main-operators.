# Дополнительное практическое задание по модулю: "Основные операторы", задание "Слишком древний шифр"

import random

def check_passcode(n):
    passdict = {}  # Cловарь с паролями для сверки.
    passdict.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645, 10: 141923283746})
    passdict.update({11: 11029384756, 12: 12131511124210394857, 13: 112211310495867, 14: 1611325212343114105968})
    passdict.update({15: 1214114232133124115106978, 16: 1317115262143531341251161079, 17: 11621531441351261171089})
    passdict.update({18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910})
    passdict.update({20: 13141911923282183731746416515614713812911})
    passcode = passdict.get(n)
    return passcode

def find_number():  # Узнаём выпадающее число из первой вставки.
    nums = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers = list(range(3, 21))
    number = random.choice(numbers)
    return number

num = find_number()
print('Число для первой вставки (подбор пароля): ', num)

# Алгоритм подбора пароля.
pairs1 = list(range(1, num))
pairs2 = list(range(1, num))
pairs = []
result = ''

for i in pairs1:
    for j in pairs2:
        psn1 = i  #  pairsnum1[i]
        psn2 = j  #  pairsnum2[j]
        if psn1 >= psn2:
            continue
        else:
            multiple = num % (psn1 + psn2)  # Проверка на кратность.
            if multiple == 0:
                pairs.append([psn1, psn2])
                result = result + str(psn1) + str(psn2)

print('Пары чисел для пароля: ', *pairs)
print('Пароль - ', result, '- для второй вставки')
if int(result) == check_passcode(num):
    print('Пароль проверен, вводите его и выходите из ловушки!')
