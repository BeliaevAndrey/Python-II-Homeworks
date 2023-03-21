# Создайте функцию-генератор.
# Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте правило:
# «число является простым, если делится нацело только на единицу и на себя»
from typing import Iterable


def gen_fun2(lim: int) -> Iterable:
    yield from (i for i in range(2, lim)
                if i == 2 or (i % 2 and
                all(i % div for div in range(3, int(i ** 0.5) + 1, 2))))


def main():
    lim = int(input('Input N: '))
    print(', '.join((str(num) for num in gen_fun2(lim))))


if __name__ == '__main__':
    main()
