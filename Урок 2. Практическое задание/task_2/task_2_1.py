"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
Для извлечения цифр числа используйте арифм. операции

Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

import sys

NUMBER = input("Введите целое число (отрицательное число будет взято по "
               "модулю) или 'q' для выхода:\n")

while True:
    if NUMBER == "q":
        sys.exit("Вы вышли из программы")
    try:
        NUMBER = abs(int(NUMBER))
        break
    except ValueError:
        NUMBER = input("Вы ввели значение, не являющееся целым числом. "
                       "Повторите попытку или введите 'q' для выхода:\n")
        continue

ODD = EVEN = 0
LEFT_NUMBER = NUMBER

while True:
    LEFT_NUMBER, CHECK_NUMBER = LEFT_NUMBER // 10, LEFT_NUMBER % 10

    if CHECK_NUMBER % 2 == 0:
        EVEN += 1
    else:
        ODD += 1

    if LEFT_NUMBER == 0:
        break

print(f"В числе {NUMBER} всего {EVEN + ODD} цифр, из которых {EVEN} чётных и "
      f"{ODD} нечётных.")
