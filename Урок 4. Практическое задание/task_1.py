"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных
данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно
оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import string
import timeit
import cProfile

"""
В качестве первой задачи для рассмотрения и оптимизации я выбрал два своих 
варианта решения задачи "House Password" с сайта https://py.checkio.org.
Условие: предложенный пользователем пароль считается достаточно стойким, если 
его длина больше или равна 10 символам, он содержит, как минимум одну цифру, 
одну букву в верхнем и одну в нижнем регистре. Пароль может содержать только 
латинские буквы и/или цифры.
Вх. данные: Пароль как строка.
Вых. данные: Безопасность пароля в виде булевого значения (bool) или любого 
типа данных, который может быть сконвертирован и представлен как булево 
значение (True или False)
"""


def old_variant():
    """
    Старый вариант решения задачи, я её делал примерно 4-5 месяцев назад.
    Для сохранения истоической достоверности, советы пайлинта (коих, на
    удивление, немного) были проигнорированы.
    Если я правильно разобрался, то сложность данного алгоритма - квадратичная
    из-за цикла for и вложенных в него методов count. Я не нашёл  детального
    описания того, как он (метод count) работает, но, полагаю, без цикла
    там не обошлось, пусть и максимально оптимизированного.
    Наибольшее количество времени при выполнении данного варианта программы
    затрачивается именно на метод count, если верить Profile, применённого к
    большому количеству вызовов программы.
    :return: None
    """

    def checkio(data: str) -> bool:
        lower_symbols = 0
        upper_symbols = 0
        digit_symbols = 0
        for symbol in data:
            if string.ascii_lowercase.count(symbol) > 0:
                lower_symbols += 1
            elif string.ascii_uppercase.count(symbol) > 0:
                upper_symbols += 1
            elif string.digits.count(symbol) > 0:
                digit_symbols += 1
            else:
                return False
        if lower_symbols > 0 and upper_symbols > 0 and \
                digit_symbols > 0 and len(data) >= 10:
            return True
        else:
            return False

    assert checkio('A1213pokl') is False
    assert checkio('bAse730onE4') is True
    assert checkio('asasasasasasasaas') is False
    assert checkio('QWERTYqwerty') is False
    assert checkio('123456123456') is False
    assert checkio('QwErTy911poqqqq') is True


def new_variant():
    """
    Среди решений других участников сайта, было одно, которое мне очень
    понравилось. В нём для решения прменялись только встроенные (а значит
    хорошо оптимизированные) методы, логические операторы и ветвление. Убрав из
    него лишние методы и заменив ветвление выражением с логическими операторами
    ИЛИ, было получено следующее решение в одну строку.
    Сложность алгоритма - линейная, причём из-за того, что реализована
    структура на логическом операторе ИЛИ, количество выполняемых операций
    варируется от 1 до 5 до перврого результата True (или все 5 False).
    :return: None
    """

    def checkio(data) -> bool:
        return not (len(data) < 10 or data.isdigit() or data.isalpha() or
                    data.islower() or data.isupper())

    assert checkio('A1213pokl') is False
    assert checkio('bAse730onE4') is True
    assert checkio('asasasasasasasaas') is False
    assert checkio('QWERTYqwerty') is False
    assert checkio('123456123456') is False
    assert checkio('QwErTy911poqqqq') is True


print("Время 1 выполнения старого варианта кода первой задачи:")
print(timeit.timeit("old_variant()", setup="from __main__ import old_variant",
                    number=1))
print("Время 1 выполнения нового варианта кода первой задачи.")
print(timeit.timeit("new_variant()", setup="from __main__ import new_variant",
                    number=1))
print("----------------")
print("Время 1000 выполнения старого варианта кода первой задачи:")
print(timeit.timeit("old_variant()", setup="from __main__ import old_variant",
                    number=1000))
print("Время 1000 выполнений нового варианта кода первой задачи:")
print(timeit.timeit("new_variant()", setup="from __main__ import new_variant",
                    number=1000))
print("----------------")
print("Время 1000000 выполнений старого варианта кода первой задачи:")
print(timeit.timeit("old_variant()", setup="from __main__ import old_variant"))
print("Время 1000000 выполнений нового варианта кода первой задачи:")
print(timeit.timeit("new_variant()", setup="from __main__ import new_variant"))
print("----------------")
# cProfile.run('print(timeit.timeit("old_variant()", '
#              'setup="from __main__ import old_variant"))')
# cProfile.run('print(timeit.timeit("new_variant()", '
#              'setup="from __main__ import new_variant"))')

"""
При выполнении небольшого числа вызовов, новый код выполняется примерно на 
порядок быстрее старого.
При увеличении количества вызовов, новый код выполняется примерно в 14 раз
быстрее старого. Наиболее наглядно это при 1 млн вызовов - при параметрах моего
компьютера это 4,28 сек против 58,61 сек.
"""

"""
В качестве второй задачия выбрал "Secret Message" с того же сайта.
Дан кусок текста. Соберите все заглавные буквы в одно слово в том порядке как 
они встречаются в куске текста. Например: текст = "How are you? Eh, ok. Low or 
Lower? Ohhh.", если мы соберем все заглавные буквы, то получим сообщение 
"HELLO".
Входные данные: Текст как строка (юникод).
Выходные данные: Секретное сообщение как строка или пустая строка.
"""


def old_variant_2():
    """
    Этот вариант я придумал сразу. Честно, что тут доводить до ума, не знаю,
    по крайней мере пока.
    :return: None
    """

    def find_message(text: str) -> str:
        """
        Сложность - скорее всего линейная. Но есть некоторые сомнения.
        В генераторе есть цикл, что логично. Метод join скорее всего тоже
        работает через цикл. Но ни один из них не является вложенным для
        другого, join срабатывает после генерации списка. Но, возможно, я
        что-то не знаю / не учитываю.
        """
        return "".join([el for el in text if el.isupper()])

    assert find_message("How are you? Eh, ok. "
                        "Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"


def new_variant_2():
    """
    Этот вариант пришлось придумывать, делая "даунгрейд" изначального. На
    удивление, это не так просто.
    :return: None
    """

    def find_message(text: str) -> str:
        """
        Сложность - скорее всего линейная. Но конкатенация - сама по себе
        медленный метод.
        """
        msg = ""
        for el in text:
            if el.isupper():
                msg += el
        return msg

    assert find_message("How are you? Eh, ok. "
                        "Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"


print("Время 1 выполнения старого варианта кода второй задачи:")
print(timeit.timeit("old_variant_2()",
                    setup="from __main__ import old_variant_2", number=1))
print("Время 1 выполнения нового варианта кода второй задачи:")
print(timeit.timeit("new_variant_2()",
                    setup="from __main__ import new_variant_2", number=1))
print("----------------")
print("Время 1000 выполнения старого варианта кода второй задачи:")
print(timeit.timeit("old_variant_2()",
                    setup="from __main__ import old_variant_2", number=1000))
print("Время 1000 выполнений нового варианта кода второй задачи:")
print(timeit.timeit("new_variant_2()",
                    setup="from __main__ import new_variant_2", number=1000))
print("----------------")
print("Время 1000000 выполнений старого варианта кода второй задачи:")
print(timeit.timeit("old_variant_2()",
                    setup="from __main__ import old_variant_2"))
print("Время 1000000 выполнений нового варианта кода второй задачи:")
print(timeit.timeit("new_variant_2()",
                    setup="from __main__ import new_variant_2"))

# cProfile.run('print(timeit.timeit("old_variant_2()", '
#              'setup="from __main__ import old_variant_2"))')
# cProfile.run('print(timeit.timeit("new_variant_2()", '
#              'setup="from __main__ import new_variant_2"))')

"""
Как это ни странно, новый подробный вариант через конкатенацию при одинаковой 
сложности алгоритмаоказался немного ыстрее выполненного через генератор 
однострочника (12,76 сек протв 12,5 сек для 1 млн выполнений). Возможно, для 
нового варианта оказалось меньшее количество операцийю. В нём, при нахождении 
удовлетворяющего условию элемента, тот сразу добавлялся к итоговой строке.
В старом - при нахохдении удовлетворяющего условию элемента, тот добавлялся в 
список, а после полученный список методом join преобразовывался в строку.
Но при столь небольшой разнице во вренемни, старый вариант кода занимает меньше
места и сохранил хорошую читаемость.
"""
