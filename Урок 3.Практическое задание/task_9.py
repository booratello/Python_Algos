"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов
матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""

from random import randrange

# Я верю в пользователя, он точно введёт числа.
ROWS = int(input("Задайте количество строк в матрице:\n"))
COLUMNS = int(input("Задайте количество столбцов в матрице:\n"))
MATRIX = [[randrange(100) for j in range(COLUMNS)] for i in range(ROWS)]

for i in MATRIX:
    print(i)

MIN_LIST = [min([MATRIX[i][j] for i in range(ROWS)]) for j in range(COLUMNS)]
print(f"Минимальные значения по столбцам:\n{MIN_LIST}")
print(f"Максимальное среди них = {max(MIN_LIST)}.")
