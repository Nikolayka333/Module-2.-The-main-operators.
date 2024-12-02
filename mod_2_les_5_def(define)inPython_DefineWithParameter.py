# Домашняя работа по уроку "Функции в Python.Функция с параметром"

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        if (n <= 0
                or m <= 0
                or value <= 0):
            matrix = []
            continue
        list_for_line = []
        for j in range(m):
            list_for_line.append(value)
        matrix.append(list_for_line)
    return matrix
result1 = get_matrix(3, 7, 1)
result2 = get_matrix(4, 5, 75)
result3 = get_matrix(5, 2, 913)
print(result1)
print(result2)
print(result3)
