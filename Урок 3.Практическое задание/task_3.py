"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""

from random import randrange

RAND_LIST = [randrange(-100, 101) for _ in range(randrange(2, 21))]
print(RAND_LIST)

MIN_IDX = RAND_LIST.index(min(RAND_LIST))
MAX_IDX = RAND_LIST.index(max(RAND_LIST))

RAND_LIST[MIN_IDX], RAND_LIST[MAX_IDX] = RAND_LIST[MAX_IDX], RAND_LIST[MIN_IDX]
print(RAND_LIST)
