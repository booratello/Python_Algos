"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

from math import ceil, log1p
from memory_profiler import profile, memory_usage
from sys import setrecursionlimit


def sieve() -> int:
    prime = 1000
    var_list = list(range(2, ceil(prime * log1p(2 * prime) + prime)))
    simple = []
    while True:
        if var_list[0] ** 2 in var_list:
            for i in var_list[var_list.index(var_list[0] ** 2): len(var_list)]:
                if i % var_list[0] == 0:
                    var_list.remove(i)
        simple.append(var_list.pop(0))
        if len(simple) >= prime:
            del var_list
            return simple[prime - 1]


def not_sieve() -> int:
    prime = 1000
    var_list = list(range(2, ceil(prime * log1p(2 * prime) + prime)))
    simple = [2]
    for i in var_list[1:]:
        buf_list = var_list[:var_list.index(i)]
        counter = 0
        for div_el in buf_list:
            if i % div_el != 0:
                counter += 1
            if counter == len(buf_list):
                simple.append(i)
                if len(simple) >= prime:
                    return simple[prime - 1]


def rec_sieve() -> int:
    setrecursionlimit(2000)

    def rec(var_list, simple):
        if var_list[0] ** 2 in var_list:
            for i in var_list[var_list.index(var_list[0] ** 2): len(var_list)]:
                if i % var_list[0] == 0:
                    var_list.remove(i)
        simple.append(var_list.pop(0))
        if len(simple) >= prime:
            return simple[prime - 1]
        return rec(var_list, simple)

    prime = 1000
    start_list = list(range(2, ceil(prime * log1p(2 * prime) + prime)))
    simple_list = []
    return rec(start_list, simple_list)


if __name__ == '__main__':
    m1 = memory_usage()
    print(f"1000е простое число равно {not_sieve()}.")
    m2 = memory_usage()
    print(f"На вариант с перебором понадобилось {m2[0] - m1[0]} MiB памяти.")
    m3 = memory_usage()
    print(f"1000е простое число равно {sieve()}.")
    m4 = memory_usage()
    print(f"На вариант с решетом понадобилось {m4[0] - m3[0]} MiB памяти.")
    m5 = memory_usage()
    print(f"1000е простое число равно {rec_sieve()}.")
    m6 = memory_usage()
    print(f"На вариант с рекурсивным понадобилось {m6[0] - m5[0]} MiB памяти.")

"""
На сколько помню, требовалось указать параметры своих ОС и ПО: 
Windows 10 Home x64, Python 3.8

Я просматирвал разые варианты предыдущих задач, но с решетом выходит всё 
наиболее наглядно, в этой задаче можно передать / получать значения, вызывающие
относительно заметный инкремент по памяти. 

Проверил 3 варианта для задачи поиска n-го простого числа: с перебором, с 
решетом и с рекурсивным решетом.
Все варианты были проверены с помощью @profile. Сейчас декораторы удалены, т.к.
они требуют дополнительной памяти и времени (что не удивительо), особенно это 
сказалось на методе с перебором. Для варианта с рекурсией, естественно, 
профилировка срабатывала на каждый вызов функции. Но нигде не было сильных 
инкрементов по памяти, везде наблюдалась примерно одинаковая картина. Для 
примера оставил профилировку для обычного решета.
  
Line #    Mem usage    Increment   Line Contents
================================================
    20     15.6 MiB     15.6 MiB   @profile
    21                             def sieve() -> int:
    22     15.6 MiB      0.0 MiB       prime = 10000
    23     19.9 MiB      4.2 MiB       var_list = list(range(2, ceil(prime 
                                                * log1p(2 * prime) + prime)))
    24     19.9 MiB      0.0 MiB       simple = []
    25                                 while True:
    26     19.9 MiB      0.0 MiB           if var_list[0] ** 2 in var_list:
    27     20.7 MiB      0.8 MiB               for i in var_list[
                                                    var_list.index(var_list[0] 
                                                    ** 2): len(var_list)]:
    28     20.7 MiB      0.0 MiB                   if i % var_list[0] == 0:
    29     20.7 MiB      0.0 MiB                       var_list.remove(i)
    30     19.8 MiB      0.0 MiB           simple.append(var_list.pop(0))
    31     19.8 MiB      0.0 MiB           if len(simple) >= prime:
    32     19.1 MiB      0.0 MiB               del var_list
    33     19.1 MiB      0.0 MiB               return simple[prime - 1]


10000е простое число равно 104729.

Прирост памяти наблюдался при объявлении объёмных списков и срезов. Что 
примечательно, в условии if var_list[0] ** 2 in var_list использовался срез, 
и для него выделяляась память, а после завершния условия, когда данный срез 
больше не требовался, память освобождалась. К сожалению, я не смог разобраться,
почему при срабатывании условия if len(simple) >= prime освобождалась 
дополнительная память, а так же почему удаление большого списка var_list не 
освободило соответствующее ему количество памяти (del тут по сути не 
срабатывает, я пробовал с ним и без него).


Для проверки выделенной под каждый вид задачи памяти использовал метод
memory_usage. Был получен следующий результат:

1000е простое число равно 7919.
На вариант с перебором понадобилось 0.2890625 MiB памяти.
1000е простое число равно 7919.
На вариант с решетом понадобилось 0.12890625 MiB памяти.
1000е простое число равно 7919.
На вариант с рекурсивным понадобилось 0.9140625 MiB памяти.

Обычное решето в данном случае снова выигрывает, как и в случае с проверкой на 
время выполнеия.
Перебор требует ощутимо больше памяти, что заметно при увеличении номера 
искомого простого числа.
Рекурсивное решето, что ожидаемо, запрашивает дополнительную память на каждый
рекурсивный вызов, в каждый из которых передаётся большой список и применяется
большой срез по нему. В результате памяти требуется в разы больше, чем даже для
перебора, что не оправдано. Так же можно превысит глубину рекурсии, а если её 
увеличить - есть шанс завершить досрочно программу с кодом 
Process finished with exit code -1073741571.
"""
