import re
import fractions


def read_fractions(frac_num: str | int = 'n') -> str:
    pattern = re.compile("\\d+/\\d+")
    while True:
        frac_str = input(f'Введите {frac_num}-ю дробь в виде "a/b":\n_> ').replace(' ', '')
        if pattern.match(frac_str):
            return frac_str
        else:
            print('Дробь введена неверно.')


def gcd(a: int, b: int) -> int:
    """
    recursive try
    :param a:
    :param b:
    :return:
    """
    return (b and gcd(b, a % b)) or a


def calc_summ(first: tuple, second: tuple) -> str:
    """
    Addition af fractions
    :param first:  tuple [int, int]
    :param second: tuple [int, int]
    :return: str
    """
    upper = first[0] * second[1] + first[1] * second[0]
    lower = first[1] * second[1]
    divisor = gcd(upper, lower)
    if lower/divisor == 1:
        return str(upper)
    return f'{int(upper / divisor)}/{int(lower / divisor)}'


def calc_mult(first: tuple, second: tuple) -> str:
    """
    Multiplication of fractions
    :param first:  tuple [int, int]
    :param second: tuple [int, int]
    :return: str
    """
    upper = first[0] * second[0]
    lower = first[1] * second[1]
    divisor = gcd(upper, lower)
    if lower/divisor == 1:
        return str(upper)
    return f'{int(upper / divisor)}/{int(lower / divisor)}'


def main():
    first = read_fractions(1)
    second = read_fractions(2)
    clc_first = tuple(map(int, first.split('/')))
    clc_second = tuple(map(int, second.split('/')))
    print('\nСложение:')
    print('Результат:', calc_summ(clc_first, clc_second))
    print('Проверка: ', fractions.Fraction(first) + fractions.Fraction(second))

    print('\nПроизведение:')
    print('Результат:', calc_mult(clc_first, clc_second))
    print('Проверка: ', fractions.Fraction(first) * fractions.Fraction(second))


if __name__ == '__main__':
    main()
