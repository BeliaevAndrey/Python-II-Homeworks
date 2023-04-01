import csv
import os


def csv_writer(in_dct: dict,
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
    data = []
    for i_key, i_val in in_dct.items():
        data.append([i_key, *i_val.values()])
    with open(file_path, 'w', encoding='utf-8') as f_out:
        write_csv = csv.writer(f_out, dialect='excel', delimiter=';')
        write_csv.writerows(data)


if __name__ == '__main__':
    print('Not for separate use')
