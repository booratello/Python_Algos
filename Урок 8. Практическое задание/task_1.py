"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.

Пример:
строка: рара

подстроки:
рар
ра
р
а
ар
ара

Итог: 6 подстрок
"""

import hashlib
from pprint import pprint

S = input("Введите строку из маленьких латинских букв:\n")
COMB_SET = set()
COMB_SET_HASH = set()

for i in range(len(S)):
    for j in range(len(S) - i):
        SUB_S = S[j:(len(S) - i)]
        if len(SUB_S) != len(S):
            COMB_SET.add(SUB_S)
            COMB_SET_HASH.add(hashlib.sha1(SUB_S.encode('utf-8')).hexdigest())

print(f"Количество уникальных подстрок: {len(COMB_SET)}")
print(f"Уникальные подстроки:")
pprint(sorted(list(COMB_SET)))
print("Хэши уникальных подстрок (порядок не соответствует списку выше):")
pprint(COMB_SET_HASH)
