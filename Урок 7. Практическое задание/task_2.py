"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644,
            12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644,
                    41.62921998361278, 46.11436617832828]
"""

from timeit import timeit
from random import random


def merge_sort_rnd(number):
    def merge_sort(some_list):
        if len(some_list) > 1:
            center = len(some_list) // 2
            left = some_list[:center]
            right = some_list[center:]

            merge_sort(left)
            merge_sort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    some_list[k] = left[i]
                    i += 1
                else:
                    some_list[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                some_list[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                some_list[k] = right[j]
                j += 1
                k += 1
            return some_list

    rnd_list = [random() * 50 for _ in range(number)]
    copy_rnd_list = rnd_list.copy()
    merge_sort(rnd_list)
    return f"Несортированный список:\n{copy_rnd_list}\n" \
           f"Сортированный список:\n{rnd_list}"


print("Пример выполнения сортировки:")
print(merge_sort_rnd(10))
print("Среднее время выполнения 1000 вызовов функции с рандомным списком из:")
print("- 10 элементов:")
print(timeit("merge_sort_rnd(10)",
             setup="from __main__ import merge_sort_rnd", number=1000))

print("- 100 элементов:")
print(timeit("merge_sort_rnd(100)",
             setup="from __main__ import merge_sort_rnd", number=1000))

print("- 1000 элементов:")
print(timeit("merge_sort_rnd(1000)",
             setup="from __main__ import merge_sort_rnd", number=1000))
