"""
Задание 5.
Пользователь вводит две буквы. Определить,
на каких местах алфавита они стоят, и сколько между ними находится букв.

Подсказка:
Вводим маленькие латинские буквы.
Обратите внимание, что ввести можно по алфавиту, например, a,z
а можно наоборот - z,a
В обоих случаях программа должна вывести корректный результат.
В обоих случаях он 24, но никак не -24
"""
import sys


def is_it_alphabetical_symbols(some_symbol):
    """
    Проверка на ввод английских букв, можно в вверхнем регистре.
    :param some_symbol: str
    :return: str
    """

    some_symbol = some_symbol.lower()
    try:
        ord(some_symbol)
    except TypeError:
        sys.exit("Вы ввели более одного символа.")
    if ord(some_symbol) < 97 or ord(some_symbol) > 122:
        sys.exit("Вы ввели символ не из английского алфавита")
    return some_symbol


print("Нужно ввести две буквы из английского алфавита.")

FIRST_CHAR = is_it_alphabetical_symbols(input("Введите первую букву:\n"))
SECOND_CHAR = is_it_alphabetical_symbols(input("Введите вторую букву:\n"))

print(f'Буква "{FIRST_CHAR}" стоит на {ord(FIRST_CHAR) - 96} '
      f'месте в английском алфавите.')
print(f'Буква "{SECOND_CHAR}" стоит на {ord(SECOND_CHAR) - 96} '
      f'месте в английском алфавите.')
print(f"Количество символов между ними: "
      f"{abs(ord(FIRST_CHAR) - ord(SECOND_CHAR)) - 1}.")
