"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля
collections
Для лучшее освоения материала можете даже сделать несколько решений этого
задания, применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши
знания по ООП (в частности по перегрузке методов)
"""
# Изобретаю велосипед
from collections import deque, ChainMap


def input_hex() -> list:
    """
    Запрос на ввод шестнадцатеричного числа в виде списка.
    """
    _ = input("Введите шестнадцатеричное число "
              "(слитно цифры от 0 до 9 и буквы от A до F):\n")
    return list(_.upper())


def to_dec(hex_num: list) -> int:
    """
    Перевод шестнадцатеричного числа в десятичное.
    """
    dec_num = 0
    counter = len(hex_num)
    for el_hex in hex_num:
        for key, value in HEX_LIST.items():
            if el_hex == value:
                counter -= 1
                dec_num += 16 ** counter * key
                break
    return dec_num


def to_hex(dec_num: int) -> list:
    """
    Перевод десятичного числа в десятичное шестнадцатеричное.
    """
    hex_num = deque([])
    while dec_num != 0:
        dec_num, remainder = dec_num // 16, dec_num % 16
        hex_num.appendleft(HEX_LIST[remainder])
    return list(hex_num)


NUM = {}
for i in range(10):
    NUM[i] = str(i)
CHAR = {}
for i in range(10, 16):
    CHAR[i] = chr(55 + i)
HEX_LIST = ChainMap(NUM, CHAR)

# Я верю в пользователя, он введёт все данные корректно.
FIRST = input_hex()
SECOND = input_hex()
print(f"Сумма: {to_hex(to_dec(FIRST) + to_dec(SECOND))}.")
print(f"Произведение: {to_hex(to_dec(FIRST) * to_dec(SECOND))}.")
