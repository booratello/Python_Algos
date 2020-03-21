"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

import sys


def is_it_int(some_var, restriction):
    """
    Проверка валидности вводимых пользователем данных.
    :param restriction: boolean
    :param some_var: str
    :return: int
    """

    if some_var == "q":
        sys.exit(f"Вы вышли из программы.")
    try:
        some_var = abs(int(some_var))
        if restriction is True and not 0 <= some_var <= 9:
            return is_it_int(input("Вы ввели число вне диапазона от 0 до 9. "
                                   "Попробуйте снова или введите 'q' для "
                                   "выхода из программы.\n"), restriction)
        return some_var
    except ValueError:
        return is_it_int(input("Вы ввели значение, не являющееся целым числом."
                               " Попробуйте снова или введите 'q' для выхода "
                               "из программы.\n"), restriction)


def rec_func_inside(num, ctrl_num, counter=0):
    """
    Функция принимает число, определяет, является последняя цифра равной
    контрольной, в случае равенства увеличивает счётчик и вызывает себя с
    параметрами из оставшейся части числа, контрольной цифры и значения
    счётчика. Рекурсия прекращается, когда оставшаяся часть числа не делится
    нацело на 10
    :param num: int
    :param ctrl_num: int
    :param counter: int
    :return: int
    """
    num, buffer_num = num // 10, num % 10
    if num != 0:
        if buffer_num == ctrl_num:
            counter += 1
    else:
        if buffer_num == ctrl_num:
            counter += 1
    return rec_func_inside(num, ctrl_num, counter) if num != 0 else counter


def rec_func_outside(total_nums, ctrl_num, counter=0, iteration=1):
    """
    Функция принимает количество цифр, контрольную цифру и вызывает себя это
    количество раз, каждый раз запрашивая новое число, вычисляя в каждом из них
    количество цифр, равных конторльной, и вычисляя итоговое количество таких
    цифр.
    :param total_nums: int
    :param ctrl_num: int
    :param counter: int
    :param iteration: int
    :return: str
    """
    num = is_it_int(input(f"Введите {iteration}е число (отрицательное число "
                          f"будет взято по модулю):\n"), False)
    counter = rec_func_inside(num, ctrl_num, counter)
    return print(f"Было введено {counter} цифр '{ctrl_num}'.") \
        if total_nums == 1 else \
        rec_func_outside(total_nums - 1, ctrl_num, counter, iteration + 1)


TOTAL_NUMS = is_it_int(input("Сколько будет чисел? Отрицательное число будет "
                             "взято по модулю.\n"), False)
CONTROL_NUM = is_it_int(input("Какую цифру считать? "
                              "Введите число от 0 до 9 (отрицательное число "
                              "будет взято по модулю):\n"), True)


rec_func_outside(TOTAL_NUMS, CONTROL_NUM)
