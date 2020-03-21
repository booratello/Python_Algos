"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

import sys
from random import randint


def is_it_int(some_var, answer):
    """
    Проверка валидности вводимых пользователем данных.
    :param answer: int
    :param some_var: str
    :return: int
    """
    while True:
        if some_var == "q":
            sys.exit(f"Вы вышли из программы. "
                     f"Мною было загадано число {answer}.")
        try:
            some_var = int(some_var)
            if not 0 <= some_var <= 100:
                some_var = input("Вы ввели число вне диапазона от 0 до 100. "
                                 "Попробуйте снова или введите 'q' для выхода "
                                 "из программы.\n")
                continue
            return some_var
        except ValueError:
            some_var = input("Вы ввели значение, не являющееся целым числом. "
                             "Попробуйте снова или введите 'q' для выхода "
                             "из программы.\n")
            continue


RND_NUM = randint(0, 100)
print("Мною загадано случайное число от 0 до 100. "
      "Попробуйте угадать его максимум за 10 попыток.")

for i in range(10, 0, -1):
    USER_ANSWER = is_it_int(input(f"Введите число от 0 до 100 или 'q' "
                                  f"для выхода. Попыток осталось: {i}.\n"),
                            RND_NUM)

    if i == 1:
        print(f"Жаль, Вы не угадали, это было число {RND_NUM}.")
    elif USER_ANSWER > RND_NUM:
        print(f"Нет, я загадал число меньше, чем {USER_ANSWER}.")
    elif USER_ANSWER < RND_NUM:
        print(f"Нет, я загадал число больше, чем {USER_ANSWER}.")
    elif USER_ANSWER == RND_NUM:
        print(f"Поздравляю, Вы угадали, это число {USER_ANSWER}!")
        break
