"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""

import sys


def is_it_real_number(some_var):
    """
    Проверка валидности вводимых пользователем данных.
    :param some_var: str
    :return: float
    """

    try:
        some_var = float(some_var)
    except ValueError:
        sys.exit("Вы ввели значение, не являющееся действительным числом.")
    return some_var


A = is_it_real_number(input("Введите первое число:\n"))
B = is_it_real_number(input("Введите второе число:\n"))
C = is_it_real_number(input("Введите третье число:\n"))

if A < B < C or A > B > C:
    print(f"Среднее число равно {B}.")
elif B < A < C or B > A > C:
    print(f"Среднее число равно {A}.")
elif A < C < B or A > C > B:
    print(f"Среднее число равно {C}.")
elif A == B == C:
    print(f"Все введённые числа одинакоые.")
else:
    print(f"Среди введённых чисел нет среднего.")
