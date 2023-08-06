from random import randint as r_int, uniform as r_unf
import csv
from hw09t02_decorators import starting_decor, dump_to_json_dec

STRINGS_LO_LIM = 10
STRINGS_HI_LIM = 100
CFT_RANGE_LO_LIM = -10
CFT_RANGE_HI_LIM = 10
SRC_FILE_NAME = 'tst_cft_src.csv'
JSON_FILENAME = 'tst_out_file.json'


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


@starting_decor(SRC_FILE_NAME)
@dump_to_json_dec(JSON_FILENAME)
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
    # print(square_eq_root(-1.54, 4.467, 9.188))
    gen_csv_rand_nums(SRC_FILE_NAME, tst_mode=False)
    results = square_eq_root()
    print('|{:^7}|{:^10}|{:^10}|{:^10}||{:^20}|'.format(*results[0]))
    print('-' * 64)
    for row in results[1:]:
        print('|{:^7}|{:<10}|{:<10}|{:<10}||{:^20}|'.format(*map(
            lambda x: x if isinstance(x, str) else str((round(x[0], 3), round(x[1], 3)))
            if isinstance(x, tuple) else str(round(x, 3)), row)))


if __name__ == '__main__':
    main()
