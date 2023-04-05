from random import randint as r_int, uniform as r_unf
import csv

STRINGS_LO_LIM = 100
STRINGS_HI_LIM = 1000
CFT_RANGE_LO_LIM = -10
CFT_RANGE_HI_LIM = 10
SRC_FILE_NAME = 'tst_cft_src.csv'
JSON_FILENAME = 'tst_out_file.json'

__all__ = [
    'gen_csv_rand_nums'
]


def gen_csv_rand_nums(file_name: str, tst_mode: bool = True) -> None:
    """
    Generates list of random floats and dumps it to a csv-file.
    :param file_name: str       -- a name of csv-file for dump a table to
    :param tst_mode: bool       -- use three values or more (test mode on/off)
    :return: None
    """
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
