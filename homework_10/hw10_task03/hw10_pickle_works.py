import pickle
import os
from datetime import datetime as dt


def pickle_writer(in_dct: [list[dict], dict],
                  path: str,
                  file_name: str) -> None:
    """
     Writes to disk binary file of dictionary passed
    :param in_dct: dict -- dictionary to write
    :param path: str -- path where binary file to write
    :param file_name: str -- file name WITHOUT extension (extension ".bin" used)
    :return: None
    """
    file_path = os.path.join(path, file_name + '.bin')
    if os.path.exists(file_path):
        file_name += '_copy_' + str(dt.now()).replace(' ', '_').replace(':', '-').split('.')[0]
        file_path = os.path.join(path, file_name + '.bin')

    with open(file_path, 'wb') as f_out:
        pickle.dump(in_dct, f_out)


def pickle_reader(file_in_path: str) -> list[dict[str]]:
    """
    Reads binary file to a list of dictionaries
    :param file_in_path: str -- path to a file to be read
    :return: list[dict[str]]
    """
    with open(file_in_path, 'rb') as f_in:
        out_lst = pickle.load(f_in, encoding='utf-8')
    return out_lst


if __name__ == '__main__':
    print('Not for separate use')
