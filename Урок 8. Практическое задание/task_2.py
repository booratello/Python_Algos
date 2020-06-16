"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""
from collections import Counter


def binary_tree(some_phrase):
    tree = Counter(some_phrase).most_common()
    while True:
        buffer = ({0: tree[-1][0], 1: tree[-2][0]},
                  tree.pop()[1] + tree.pop()[1])
        if len(tree) != 0:
            for idx, el in enumerate(tree):
                if el[1] >= buffer[1] and idx != len(tree) - 1:
                    continue
                elif el[1] < buffer[1]:
                    tree.insert(idx, buffer)
                    break
                else:
                    tree.append(buffer)
                    break
        else:
            tree = buffer
            break
    return tree[0]


def research_tree(tree, code=''):
    if not isinstance(tree, dict):
        CODE_TABLE[tree] = code
    else:
        research_tree(tree[0], code=f'{code}0')
        research_tree(tree[1], code=f'{code}1')


CODE_TABLE = {}
S = input("Введите строку из трех слов:\n")
research_tree(binary_tree(S))
for i in S:
    print(CODE_TABLE[i], end=' ')

"""
Для фразы из примера результат будет отличаться от результата в моём варианте
(как и для прочих результатов), т.к. я использую другой механизм сортировки
частоты символов. Иерархия сохраняется, но итоговый код буквы может отличаться,
т.к. буквы с одинаковой частотой могут оказаться в листьях других узлов, в
отличие от вашего варианта.

Фраза "beep boop beer!":
Ваш вариант таблицы кодировки:
{'b': '00', ' ': '010', 'o': '011', 'r': '1000',
'!': '1001', 'p': '101', 'e': '11'}
Мой вариант таблицы кодировки:
{'b': '00', ' ': '010', 'p': '011', '!': '1000',
'r': '1001', 'o': '101', 'e': '11'}
Ваш результат кодирования фразы:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
Мой результат кодирования фразы:
00 11 11 011 010 00 101 101 011 010 00 11 11 1001 1000
"""
