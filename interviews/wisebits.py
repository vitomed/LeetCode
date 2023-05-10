"""1
Напишите функцию, печатающую последовательность чисел от 1 до 100.
Вместо чисел кратных 3, программа должна печатать FIZZ.
Вместо чисел кратных 5 - BUZZ.
Если число кратно 3 и 5 - программа должна печатать FIZZBUZZ.
"""
import time

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")

    else:
        print(i)

"""2
Напишите функцию, которая
на вход принимает многомерный список неограниченной вложенности, 
а возвращает одномерный, линеаризованный список. 
"""


def f(lst):
    f_list = []
    for item in lst:
        if isinstance(item, list):
            f_list.extend(f(item))
        else:
            f_list.append(item)

    return f_list


def f_gen(lst):
    for item in lst:
        if isinstance(item, list):
            yield from f_gen(item)

        else:
            yield item


"""3
Напишите cache декоратор для функции.
"""


def cache(func):
    results = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in results:
            results[key] = func(*args, **kwargs)
        return results[key]

    return wrapper


@cache
def my_f(sec):
    time.sleep(sec)
    return sec


if __name__ == '__main__':
    a = [[1, 2, [3, 4]]]
    assert f(a) == [1, 2, 3, 4]
    assert f_gen(a) == [1, 2, 3, 4]

    start = time.time()
    my_f(4)
    my_f(4)
    print(time.time() - start)
