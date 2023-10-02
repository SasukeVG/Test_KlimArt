import numpy as np

def input_array():
    n = int(input("Введите размер массива: "))
    Mass_X = []
    for i in range(n):
        Mass_X.append(int(input("Введите элемент массива: ")))
    return Mass_X

summ = 0
Mass_X = input_array()
for i in range(len(Mass_X)):
    summ += Mass_X[i]

print(summ)

# создание массива массивов

M = int(input("Введите количество массивов: "))
combo = []

for j in range(M):
    Mass_Rand = input_array()
    combo.append(Mass_Rand)

# Сумма элементов массивов

# max_length = max(len(arr) for arr in combo)
arrays_padded = [arr + [0] * (len(Mass_X)  - len(arr)) for arr in combo]
Mass_Z = [sum(x) for x in zip(*arrays_padded)]

print(Mass_Z)

# Поиск Массива Y

Mass_Y = np.zeros(len(Mass_X))

max_Mass_Z = max(Mass_Z)
id_of_max = Mass_Z.index(max_Mass_Z)
k = max_Mass_Z / Mass_X[id_of_max]

for i in range(len(Mass_X)):
    if Mass_Z[i] / Mass_X[i] != k:
        Mass_Y[i] = k * Mass_X[i] - Mass_Z[i]
    else:
        Mass_Y[i] = 0

print(Mass_Y)