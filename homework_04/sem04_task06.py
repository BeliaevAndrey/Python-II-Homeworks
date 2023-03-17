# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

def function(lst_in: list[int],
             idx_lo: int,
             idx_up: int):
    if idx_lo > idx_up:
        return 0
    if idx_lo < 0:
        idx_lo = -1
    return sum(lst_in[idx_lo + 1:idx_up])


def gen_list(lst_ln: int = 100,
             lim_lo: int = 0,
             lim_up: int = 100,
             ) -> list[int]:
    """
    Generating list of random integers
    :param lst_ln: list length
    :param lim_lo: lower limit for element
    :param lim_up: upper limit for element
    :return: list[int]
    """
    from random import randint as rnd_i
    lim_lo, lim_up = sorted((lim_lo, lim_up))
    return [rnd_i(lim_lo, lim_up) for _ in range(lst_ln)]


def main():
    print(res := function(
        lst_in=list(range(0, 20)),
        idx_lo=1,
        idx_up=5, ),
          res == sum([2, 3, 4, ]))

    print(res := function(
        lst_in=list(range(0, 20)),
        idx_lo=10,
        idx_up=50, ),
          res == sum([11, 12, 13, 14, 15, 16, 17, 18, 19, ]))

    print(res := function(
        lst_in=list(range(0, 20)),
        idx_lo=-10,
        idx_up=5, ),
          res == sum([*range(0, 5)]))

    print(function(gen_list(), 10, 20))


if __name__ == '__main__':
    main()
