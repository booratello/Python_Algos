"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным
образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий
его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

from random import randint
from timeit import timeit
from statistics import median

"""
Каюсь, подглядел этот вариант на просторах Интернета в реализации С++. Мои
варианты были по итогу близки п быстрой сортировке. Решил реализовать через
счётчики, вариант с делением на списки излишен.
Переделал под Python, и долго размышлял, как он работает, и почему
не всегда даёт результат. Логику примерно понял, с резульатом ситуация
следующая: он всегда будет для списка без повторений, а с если они есть -
то тут как повезёт. Не идеально, в общем. К сожалению, довести до ума не
получилось.
"""


def iterate_median(some_list):
    for i in some_list:
        cnt1 = cnt2 = 0
        for j in some_list:
            if j != i:
                if j > i:
                    cnt1 += 1
                else:
                    cnt2 += 1
        if cnt1 == cnt2:
            return f"Медиана, вычисленная перебором и сравнением: {i}"
    return "Не повезло, перебор не дал результата для этого списка."


def cocktail_sort_median(some_list):
    left = 0
    right = len(some_list) - 1
    while left <= right:
        for i in range(left, right):
            if some_list[i] > some_list[i + 1]:
                some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
        right -= 1
        for i in range(right, left, -1):
            if some_list[i - 1] > some_list[i]:
                some_list[i], some_list[i - 1] = some_list[i - 1], some_list[i]
        left += 1
    find_median = some_list[len(some_list) // 2]
    return f"Медиана, вычисленная через шейкерную сортировку: {find_median}"


RND_LIST = [randint(0, 50) for _ in range(15)]
COPY_RND_LIST = RND_LIST.copy()

print(f"Рандомный список:\n{RND_LIST}")
print(f"Медиана, вычисленная модулем statistics: {median(RND_LIST)}")
print(iterate_median(RND_LIST))
print(cocktail_sort_median(RND_LIST))

print("Время поиска медианы методом перебора:")
print(timeit("iterate_median(RND_LIST)",
             setup="from __main__ import iterate_median, RND_LIST", number=1))
print("Время поиска медианы через шейкерную сортировку:")
print(timeit("cocktail_sort_median(COPY_RND_LIST)",
             setup="from __main__ import cocktail_sort_median, COPY_RND_LIST",
             number=1))

"""
Резульат замеров времени получился неоднозначным. Иногда перебор оказывался в
2 раза быстрее сортировки (у неё всегда примерно одинаковое время выполнения),
иногда - на порядок медленнее. Это зависит от того, с какой итерации перебора
получиться выйти на услвие cnt1 == cnt2, чем раньше - тем меньше времени в
итоге это займет.
"""
