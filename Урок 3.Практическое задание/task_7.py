"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и
различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""

from random import randrange

RAND_LIST = [randrange(-30, 31) for _ in range(20)]
print(RAND_LIST)

FIRST_MIN = min(RAND_LIST)
COUNTER = RAND_LIST.count(FIRST_MIN)
RAND_LIST.remove(FIRST_MIN)
SECOND_MIN = min(RAND_LIST)

print(f"Наименьший элемент: {FIRST_MIN}, встречается в этоим списке {COUNTER}"
      f" раз.\nВторой наименьший элемент: {SECOND_MIN}.")
