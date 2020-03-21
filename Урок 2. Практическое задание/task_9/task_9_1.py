"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
Если у нескольких чисел одинаковая сумма цифр, вывести наибольшее из них.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

import sys


def is_it_int(some_var):
    """
    Проверка валидности вводимых пользователем данных.
    :param some_var: str
    :return: int
    """
    while True:
        if some_var == "q":
            sys.exit(f"Вы вышли из программы.")
        try:
            some_var = abs(int(some_var))
            return some_var
        except ValueError:
            some_var = input("Вы ввели значение, не являющееся целым числом. "
                             "Попробуйте снова или введите 'q' для выхода "
                             "из программы.\n")
            continue


TOTAL_NUMS = is_it_int(input("Сколько будет чисел? Отрицательное число будет "
                             "взято по модулю.\n"))
MAX_NUM = 0
MAX_COUNT = 0


for i in range(1, TOTAL_NUMS + 1):
    NOW_NUM = NUM = is_it_int(input(f"Введите {i}е число (отрицательное число "
                                    f"будет взято по модулю):\n"))
    COUNTER = 0

    while True:
        NUM, BUFFER_NUM = NUM // 10, NUM % 10

        if NUM != 0:
            COUNTER += BUFFER_NUM
        else:
            COUNTER += BUFFER_NUM
            break

    if COUNTER > MAX_COUNT or COUNTER == MAX_COUNT and NOW_NUM > MAX_NUM:
        MAX_NUM, MAX_COUNT = NOW_NUM, COUNTER

print(f"Наибольшая сумма цифр среди введённых чисел равно {MAX_COUNT}. "
      f"Наибольшее число с такой суммой равно '{MAX_NUM}'.")
