import json
import os
from datetime import datetime as dt


def json_writer(in_dct: [list, dict],
                path: str,
                file_name: str) -> None:
    """
     Writes to disk json file of dictionary passed
    :param in_dct: dict -- dictionary to write
    :param path: str -- path where binary file to write
    :param file_name: str -- file name WITHOUT extension (extension ".json" used)
    :return: None
    """
    file_path = os.path.join(path, file_name + '.json')
    if os.path.exists(file_path):
        file_name += '_copy_' + str(dt.now()).replace(' ', '_').replace(':', '-').split('.')[0]
        file_path = os.path.join(path, file_name + '.json')

    with open(file_path, 'w', encoding='utf-8') as f_out:
        json.dump(in_dct, f_out, indent=4)


def json_reader(file_path: str) -> dict[str]:
    """
    Reads json file to a dictionary
    :param file_path: str -- path to a file to be read
    :return: dict[str] -- deserialized dictionary
    """
    with open(file_path, 'r', encoding='utf-8') as f_in:
        json_dict = json.load(f_in)
    return json_dict


if __name__ == '__main__':
    print('Not for separate use')
