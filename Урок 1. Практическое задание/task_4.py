"""
Задание 4. Написать программу, которая генерирует в указанных пользователем
границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти
символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f'
включительно.

Подсказка:
Нужно обойтись без ф-ций randint() и uniform()
Использование этих ф-ций = задание не засчитывается

Функцию random() использовать можно
Опирайтесь на пример к уроку
"""

from random import random
import sys


def validation(border, task_num):
    """
    Проверка данных в зависимости от выбраной задачи.
    :param border: str
    :param task_num: int
    :return: int if task_num = 1
             float if task_num = 2
             str if task_num = 3
    """
    try:
        if task_num == 1:
            border = int(border)
        elif task_num == 2:
            border = float(border)
        else:
            border = ord(border.lower())
            if border < 97 or border > 122:
                sys.exit("Вы ввели символ не из английского алфавита")
    except ValueError:
        sys.exit(f'Вы ввели значение, не являющееся '
                 f'{"целым" if task_num == 1 else "вещественным"} числом.')
    except TypeError:
        sys.exit("Вы ввели более одного символа.")
    return border


TASK_NUM = validation((input("Какую задачу выполнить?\n"
                             "[1] Сгенерировать случайное целое число в "
                             "указанных границах;\n"
                             "[2] Сгенерировать случайное вещественное число "
                             "в указанных границах;\n"
                             "[3] Сгенерировать случайный символ из "
                             "английского алфавита в указанных границах;\n"
                             "[любое другое число] Завершить программу.\n")),
                      1)

if not 1 <= TASK_NUM <= 3:
    sys.exit("Вы вышли из программы.")

MIN_BORDER = validation(input("Введите нижнюю границу:\n"), TASK_NUM)
MAX_BORDER = validation(input("Введите верхнюю границу:\n"), TASK_NUM)

if MIN_BORDER > MAX_BORDER:
    MIN_BORDER, MAX_BORDER = MAX_BORDER, MIN_BORDER

if TASK_NUM != 2:
    RAND_RES = int(random() * (MAX_BORDER - MIN_BORDER + 1)) + MIN_BORDER
else:
    RAND_RES = round((random() * (MAX_BORDER - MIN_BORDER) + MIN_BORDER), 3)

print(f"Вы получили следующее значение из диапазона между "
      f"{MIN_BORDER if TASK_NUM != 3 else chr(MIN_BORDER)} и "
      f"{MAX_BORDER if TASK_NUM != 3 else chr(MAX_BORDER)}: "
      f"{RAND_RES if TASK_NUM != 3 else chr(RAND_RES)}.")
