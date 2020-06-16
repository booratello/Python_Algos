"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

from random import randrange

RAND_LIST = [randrange(11) for _ in range(10)]
print(RAND_LIST)

# Если нет повторяющихся чисел - вернёт первый элемент (или если первый
# элемент повторяется).
print(max(RAND_LIST, key=lambda x: RAND_LIST.count(x)))

# Pylint не доволен: Lambda may not be necessary (unnecessary-lambda), но как
# без лямбды в параметре key решить - не озарило.
