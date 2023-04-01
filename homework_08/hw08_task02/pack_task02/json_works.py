import json
import os


def json_writer(in_dct: dict,
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
    with open(file_path, 'w', encoding='utf-8') as f_out:
        json.dump(in_dct, f_out, indent=4)


if __name__ == '__main__':
    print('Not for separate use')
