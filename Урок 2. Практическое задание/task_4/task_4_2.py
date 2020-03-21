"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

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
        return validation(input("Вы ввели значение, не являющееся числом. "
                                "Повторите попытку или введите 'q' для "
                                "выхода:\n"))


def rec_func(num, sum_el=0.0, series_num=1.0, counter=0):
    """
    Функция принимает число и вызывает себя, передавая в параметры исходное
    число, уменьшенное на 1,сумму элементов ряда и значение следующего элемента
    ряда. Выход из рекурсии осуществляется, когда исходное число становится
    равным нолю.
    :param num: int
    :param sum_el: float
    :param series_num: float
    :param counter: int
    :return: str
    """
    return rec_func(num - 1, sum_el + series_num, -1 * series_num / 2,
                    counter + 1) if num != 0 else \
        print(f"Количество элементов ряда - {counter}, их сумма - {sum_el}.")


NUMBER = validation(input("Введите целое число для определения количества "
                          "элементов ряда (отрицательное число будет взято по "
                          "модулю) или 'q' для выхода:\n"))
rec_func(NUMBER)
