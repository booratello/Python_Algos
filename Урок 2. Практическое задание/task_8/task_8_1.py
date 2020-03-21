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

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

import sys


def is_it_int(some_var, restriction):
    """
    Проверка валидности вводимых пользователем данных.
    :param restriction: boolean
    :param some_var: str
    :return: int
    """
    while True:
        if some_var == "q":
            sys.exit(f"Вы вышли из программы.")
        try:
            some_var = abs(int(some_var))
            if restriction is True and not 0 <= some_var <= 9:
                some_var = input("Вы ввели число вне диапазона от 0 до 9. "
                                 "Попробуйте снова или введите 'q' для выхода "
                                 "из программы.\n")
                continue
            return some_var
        except ValueError:
            some_var = input("Вы ввели значение, не являющееся целым числом. "
                             "Попробуйте снова или введите 'q' для выхода "
                             "из программы.\n")
            continue


TOTAL_NUMS = is_it_int(input("Сколько будет чисел? Отрицательное число будет "
                             "взято по модулю.\n"), False)
CONTROL_NUM = is_it_int(input("Какую цифру считать? "
                              "Введите число от 0 до 9 (отрицательное число "
                              "будет взято по модулю):\n"), True)

COUNTER = 0
for i in range(1, TOTAL_NUMS + 1):
    NUM = is_it_int(input(f"Введите {i}е число (отрицательное число будет "
                          f"взято по модулю):\n"), False)

    while True:
        NUM, BUFFER_NUM = NUM // 10, NUM % 10

        if NUM != 0:
            if BUFFER_NUM == CONTROL_NUM:
                COUNTER += 1
        else:
            if BUFFER_NUM == CONTROL_NUM:
                COUNTER += 1
            break

print(f"Было введено {COUNTER} цифр '{CONTROL_NUM}'.")
