"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то
завершение. Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

from timeit import timeit
from random import randint


def bubble_sort(some_list):
    number = 1
    while number < len(some_list):
        for i in range(len(some_list) - number):
            if some_list[i] < some_list[i + 1]:
                some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
        number += 1
    return some_list


def bubble_sort_mod(some_list):
    number = 1
    while number < len(some_list):
        check = True
        for i in range(len(some_list) - number):
            if some_list[i] < some_list[i + 1]:
                some_list[i], some_list[i + 1], check = \
                    some_list[i + 1], some_list[i], False
        if check:
            break
        number += 1
    return some_list


RND_LIST = [randint(-100, 100) for _ in range(20)]
print(f"Рандомный список:\n{RND_LIST}")
COPY_RND_LIST = RND_LIST.copy()
print(f"Копия рандомного списка:\n{COPY_RND_LIST}")
print("Время сортировки рандомного списка стандарным методом пузырька:")
print(timeit("bubble_sort(RND_LIST)",
             setup="from __main__ import bubble_sort, RND_LIST", number=1))
print("Время сортировки копии рандомного списка модифицированным "
      "методом пузырька:")
print(timeit("bubble_sort_mod(COPY_RND_LIST)",
             setup="from __main__ import bubble_sort_mod, COPY_RND_LIST",
             number=1))
print(f"Отсортированный по убыванию рандомный список "
      f"(стандарный метод пузырька):\n{RND_LIST}")
print(f"Отсортированная по убыванию копия рандомного списка "
      f"(метод пузырька с пропуском лишних итераций):\n{COPY_RND_LIST}")

"""
Пришлось делать копию списка для второй функции и замерять время одного
выполнения - в других случаях или список передаётся уже отсортированный, или
в каждую функцию подавать рандомные, а значит разные, списки - замеры будут
не честными.

Второй метод даёт неоднозначный результат - там многое заисит от количества
элементов в списке и на сколько он получился близким к требуемой сортировке.
Если он уже несколько отсортирован, может получиться заметное ускорене
выполнения, если "лишних" итераций не будет - получаем замедление выполнения
из-за большого количества дополнительных операций присвоения и сверки.
"""
