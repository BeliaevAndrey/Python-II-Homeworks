import csv
import os
from datetime import datetime as dt


def csv_writer(in_dct: [list[dict], dict],
               path: str,
               file_name: str) -> None:
    """
     Writes to disk csv file of dictionary passed, ";" used as delimiter
    :param in_dct: dict -- dictionary to write
    :param path: str -- path where binary file to write
    :param file_name: str -- file name WITHOUT extension (extension ".csv" used)
    :return: None
    """
    file_path = os.path.join(path, file_name + '.csv')
    if os.path.exists(file_path):
        file_name += '_copy_' + str(dt.now()).replace(' ', '_').replace(':', '-').split('.')[0]
        file_path = os.path.join(path, file_name + '.csv')

    if isinstance(in_dct, list):
        data = _form_lst(in_dct)
    else:
        data = []
        for i_key, i_val in in_dct.items():
            if isinstance(i_val, dict):
                for j_key, j_val in i_val.items():
                    data.append([i_key, j_key, j_val])
            else:
                data.append([i_key, i_val])
    with open(file_path, 'w', encoding='utf-8') as f_out:
        write_csv = csv.writer(f_out, dialect='excel', delimiter=';')
        write_csv.writerows(data)


def _form_lst(data_lst: list[dict]) -> list[list[str]]:
    out_lst = [[i_key for i_key in data_lst[0].keys()]]
    for dct in data_lst:
        out_lst.append([*dct.values()])
    return out_lst


def csv_reader(file_path: str) -> list[dict[str]]:
    """
    Reads a csv file with headers to list of dicts
    :param file_path: str -- path to a file to be read
    :return: list[dict[str]]
    """
    out_dict_list = []
    with open(file_path, 'r', encoding='utf-8') as f_in:
        read_csv = csv.DictReader(f_in, dialect='excel', delimiter=';')
        keys = (next(read_csv))
        for row in read_csv:
            out_dict_list.append({key: item for key, item in zip(keys, row)})
    return out_dict_list


if __name__ == '__main__':
    print('Not for separate use')
