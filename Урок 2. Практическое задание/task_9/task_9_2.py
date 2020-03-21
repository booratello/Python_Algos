"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
Если у нескольких чисел одинаковая сумма цифр, вывести наибольшее из них.

Пример:
Введите количество чисел: 2
Введите число: 23
Введите число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
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
        some_var = abs(int(some_var))
        return some_var
    except ValueError:
        return validation(input("Вы ввели значение, не являющееся целым "
                                "числом. Повторите попытку или введите 'q' "
                                "для выхода:\n"))


def rec_func_inside(num, counter):
    """
    Функция принимает число, прибавляет значение последней цифры к счётчику,
    и вызывает себя с параметрами из оставшейся части числа и значения
    счётчика. Рекурсия прекращается, когда оставшаяся часть числа не делится
    нацело на 10.
    :param num: int
    :param counter: int
    :return: int
    """
    num, buffer_num = num // 10, num % 10
    if num != 0:
        counter += buffer_num
    else:
        counter += buffer_num
    return rec_func_inside(num, counter) if num != 0 else counter


def rec_func_outside(total_nums, max_num=0, max_count=0, iteration=1):
    """
    Функция принимает количество цифр и вызывает себя это количество раз,
    каждый раз запрашивая новое число и проводя среди них отбор с наибольшей
    суммой цифр и наибольшего из них при равной наибольшей сумме цифр.
    :param total_nums: int
    :param max_num: int
    :param max_count: int
    :param iteration: int
    :return: str
    """
    num = validation(input(f"Введите {iteration}е число (отрицательное число "
                           f"будет взято по модулю):\n"))
    counter = 0
    counter = rec_func_inside(num, counter)

    if counter > max_count or counter == max_count and num > max_num:
        max_num, max_count = num, counter

    return print(f"Наибольшая сумма цифр среди введённых чисел равно "
                 f"{max_count}.Наибольшее число с такой суммой равно "
                 f"'{max_num}'.") if total_nums == 1 else \
        rec_func_outside(total_nums - 1, max_num, max_count, iteration + 1)


TOTAL_NUMS = validation(input("Сколько будет чисел? Отрицательное число будет "
                              "взято по модулю.\n"))
rec_func_outside(TOTAL_NUMS)
