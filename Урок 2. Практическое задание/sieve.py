"""
Задача "Решето Эратосфена". Дан ряд из натуральных чисел, начинающийся с 2х.
Нужно оставить в этом ряду только простые числа.
"""

import sys


def validation(some_var):
    """
    Проверка валидности вводимых пользователем данных.
    :param some_var: str
    :return: int
    """
    if some_var == "q":
        sys.exit("Вы вышли из программы")
    try:
        some_var = int(some_var)
        if some_var < 3:
            return validation(input("Нужно ввести число больше 2х. "
                                    "Повторите попытку или введите 'q' для "
                                    "выхода:\n"))
        return some_var
    except ValueError:
        return validation(input("Вы ввели значение, не являющееся целым "
                                "числом. Повторите попытку или введите 'q' "
                                "для выхода:\n"))


def sieve(var_list, min_from_var_list):
    """
    Функция принимает исходный список и его минимальное значение; в диапазоне
    от следующего после минимального по индексу элемента до конца списка ищет и
    удаляет числа, делящиеся нацело на минимальное. После этого она вызывает
    саму себя, передавая в качестве параметров оставшуюся часть списка и
    следующий после минимального по индексу в оставшемся списке элемент.
    Рекурсивные вызовы прекращаются, когда текущее значение перебираемого
    'минимального' значения в квадрате окажется больше максимального значения
    в списке.
    :param var_list: list of int
    :param min_from_var_list: int
    :return: str
    """
    for i in var_list[var_list.index(min_from_var_list) + 1: len(var_list)]:
        if i % min_from_var_list == 0:
            var_list.remove(i)
    return sieve(var_list, var_list[var_list.index(min_from_var_list) + 1]) \
        if min_from_var_list ** 2 < max(var_list) else \
        print(f"В данном ряду простыми являютя следующие числа:\n{var_list}")


MAX_NUM = validation(input("Ведите максимальное значение исходного списка "
                           "(целое положительное число больше) 2х:\n"))


START_LIST = list(range(2, MAX_NUM + 1))

print(f"Получен список от 2 до {MAX_NUM}.")

sieve(START_LIST, min(START_LIST))
