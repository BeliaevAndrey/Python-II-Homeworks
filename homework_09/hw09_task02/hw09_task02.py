from random import randint as r_int, uniform as r_unf
import csv
# from typing import Any
from hw09t02_decorators import starting_decor

STRINGS_LO_LIM = 100
STRINGS_HI_LIM = 1000
CFT_RANGE_LO_LIM = -10
CFT_RANGE_HI_LIM = 10
SRC_FILE_NAME = 'tst_cft_src.csv'


def gen_csv_rand_nums(file_name: str, tst_mode: bool = True) -> None:
    coefficients_lst = [['No', 'a', 'b', 'c', ], ]
    for i in ([0, 1, 2] if tst_mode else range(r_int(STRINGS_LO_LIM, STRINGS_HI_LIM))):
        coefficients_lst.append([
            i + 1,
            r_unf(CFT_RANGE_LO_LIM, CFT_RANGE_HI_LIM),
            r_unf(CFT_RANGE_LO_LIM, CFT_RANGE_HI_LIM),
            r_unf(CFT_RANGE_LO_LIM, CFT_RANGE_HI_LIM),
        ])
    with open(file_name, 'w', encoding='utf-8') as f_out:
        write_csv = csv.writer(f_out, dialect='excel', delimiter=';')
        write_csv.writerows(coefficients_lst)

#
# def read_csv_rand_nums(file_name: str) -> list[list[str, int]]:
#     coefficients = []
#     with open(file_name, 'r', encoding='utf-8') as f_in:
#         read_csv = csv.reader(f_in, dialect='excel', delimiter=';')
#         coefficients.append(next(read_csv))
#         for row in read_csv:
#             coefficients.append([int(row[0])] + [*map(float, row[1:])])
#     return coefficients


@starting_decor(SRC_FILE_NAME)
def square_eq_root(a_cft: float, b_cft: float, c_cft: float) -> [float, tuple[float, float], None]:
    """
    Finds roots of square equation
    a * x**2 + b * x + c = 0           -- common equation view
    D=b^2 - 4ac                        -- equation for discriminant
    x(1,2) = (-b +/- sqrt(D)) / 2a     -- equations for roots
    :param a_cft: float                -- a coefficient
    :param b_cft: float                -- b coefficient
    :param c_cft: float                -- c coefficient
    :return: tuple[float, float] -- two roots; float -- one root; None -- no roots
    """
    discriminant = b_cft ** 2 - 4 * (a_cft * c_cft)
    if discriminant < 0:
        return 'No real roots'
    x1 = (-b_cft + discriminant ** 0.5) / (2 * a_cft)
    x2 = (-b_cft - discriminant ** 0.5) / (2 * a_cft)
    return x1, x2


def main():
    print(square_eq_root(-1.54, 4.467, 9.188))
    gen_csv_rand_nums(SRC_FILE_NAME, False)
    # cft: list[Any] = read_csv_rand_nums('tst_cft_src.csv')
    # cft[0].append('Result')
    # for row in cft[1:]:
    #     row.append(square_eq_root(*row[1:]))
    results = square_eq_root()
    # for row in results[1:]:
    #     print(*row, sep='\t')
    print('|{:^7}|{:^10}|{:^10}|{:^10}||{:^20}|'.format(*results[0]))
    print('-' * 64)
    for row in results[1:]:
        print('|{:^7}|{:<10}|{:<10}|{:<10}||{:^20}|'.format(*map(
            lambda x: x if isinstance(x, str) else str((round(x[0], 3), round(x[1], 3)))
            if isinstance(x, tuple) else str(round(x, 3)), row)))


if __name__ == '__main__':
    main()
