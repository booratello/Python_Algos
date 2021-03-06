"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем
соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

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


def rec_func(num, odd=0, even=0):
    """
    Функция принимает число, определяет, является последняя цифра числа
    чётной или нечётной, и вызвыает саму себя, передавая в параметрах результат
    деления исходного числа на 10 нацело и количества чётных и нечётных цифр.
    Выход из рекурсии осуществляется, когда результат деления числа нацело
    на 10 равен 0.
    :param num: int
    :param odd: int
    :param even: int
    :return: str
    """

    left_number, check_number = num // 10, num % 10

    if check_number % 2 == 0:
        even += 1
    else:
        odd += 1

    return rec_func(left_number, odd, even) if left_number != 0 else \
        print(f"В числе {num} всего {even + odd} цифр, из которых {even} "
              f"чётных и {odd} нечётных.")


NUMBER = validation(input("Введите целое число (отрицательное число будет "
                          "взято по модулю) или 'q' для выхода:\n"))

rec_func(NUMBER)
