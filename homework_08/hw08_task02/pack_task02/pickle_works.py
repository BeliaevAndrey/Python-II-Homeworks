import pickle
import os


def pickle_writer(in_dct: dict,
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
    with open(file_path, 'wb') as f_out:
        pickle.dump(in_dct, f_out)


if __name__ == '__main__':
    print('Not for separate use')
