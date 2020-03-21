"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
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

    if some_var == "q":
        sys.exit(f"Вы вышли из программы. Мною было загадано число {answer}.")
    try:
        some_var = int(some_var)
        if not 0 <= some_var <= 100:
            return is_it_int(input("Вы ввели число вне диапазона от 0 до 100. "
                                   "Попробуйте снова или введите 'q' для "
                                   "выхода из программы.\n"), answer)
        return some_var
    except ValueError:
        return is_it_int(input("Вы ввели значение, не являющееся целым числом."
                               " Попробуйте снова или введите 'q' для выхода "
                               "из программы.\n"), answer)


def rec_func(answer, counter=10):
    """
    Функция принммает случайное целое число, опрашивает пользователя и, или
    в случае верного ответа возвращает сообщение с поздравлениеи, или вызывает
    саму себя, уменьшая счётчик - если счётчик достигнет значения "1", то
    возвращает сообщене о проигрыше.
    :param answer: int
    :param counter: int
    :return: str
    """
    user_answer = is_it_int(input(f"Введите число от 0 до 100 или 'q' для "
                                  f"выхода. Попыток осталось: {counter}.\n"),
                            answer)
    if user_answer > answer:
        print(f"Нет, я загадал число меньше, чем {user_answer}.")
    elif user_answer < answer:
        print(f"Нет, я загадал число больше, чем {user_answer}.")
    elif user_answer == answer:
        return print(f"Поздравляю, Вы угадали, это число {user_answer}!")
    return rec_func(answer, counter - 1) if counter != 1 else \
        print(f"Жаль, Вы не угадали, это было число {answer}.")


RND_NUM = randint(0, 100)
print("Мною загадано случайное число от 0 до 100. "
      "Попробуйте угадать его максимум за 10 попыток.")
rec_func(RND_NUM)
