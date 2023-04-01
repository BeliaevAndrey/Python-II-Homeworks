# Соберите из созданных на уроке и в рамках домашнего
# задания функций пакет для работы с файлами разных форматов.
import os
from typing import Callable

from pack_task02 import (csv_reader, csv_writer,
                         json_reader, json_writer,
                         pickle_reader, pickle_writer,
                         )


def list_files(start_path: str,
               file_ext: str, ) -> list[str]:
    if 'pickle' in file_ext:
        file_ext = file_ext.replace('pickle', 'bin')
    if '.' not in file_ext:
        file_ext = '.' + file_ext
    result_lst = [file_ext]
    for path_tlp in os.walk(start_path):
        for item in path_tlp[2]:
            if item.endswith(file_ext):
                result_lst.append(os.path.join(path_tlp[0], item))
    return result_lst


def pair_converter(src_fun: Callable,
                   dst_fun: Callable,
                   src_path: str,
                   dst_path: str, ) -> None:
    data_in = src_fun(src_path)
    dst_name = (os.path.split(src_path)[-1]).split('.')[0]
    dst_fun(data_in, dst_path, dst_name)


def convert_files(file_lst: list,
                  dst_file_type: str,
                  dst_path: str, ) -> None:
    if 'pickle' in dst_file_type:
        print("Extension '.bin' will be used")
        dst_file_type = 'bin'
    if '.' not in dst_file_type:
        dst_file_type = '.' + dst_file_type

    src_ext = file_lst.pop(0)
    for file_path in file_lst:
        match (src_ext, dst_file_type):
            case ('.json', '.csv'):
                pair_converter(json_reader, csv_writer, file_path, dst_path)
            case ('.json', '.bin'):
                pair_converter(json_reader, pickle_writer, file_path, dst_path)
            case ('.csv', '.json'):
                pair_converter(csv_reader, json_writer, file_path, dst_path)
            case ('.csv', '.bin'):
                pair_converter(csv_reader, pickle_writer, file_path, dst_path)
            case ('.bin', '.json'):
                pair_converter(pickle_reader, json_writer, file_path, dst_path)
            case ('.bin', '.csv'):
                pair_converter(pickle_reader, csv_writer, file_path, dst_path)
            case _:
                raise ValueError("Unknown types:" + f'{(src_ext, dst_file_type)}')


def main():
    path_in = '/home/andrew/Documents/geekbrains/Python2023/Lections/Seminars/seminar_08/'
    path_out = os.path.join(os.getcwd(), 'tst_out')
    convert_files(file_lst=list_files(path_in, 'json'),
                  dst_file_type='pickle',
                  dst_path=path_out)

    convert_files(file_lst=list_files(path_in, 'json'),
                  dst_file_type='csv',
                  dst_path=path_out)

    convert_files(file_lst=list_files(path_in, 'bin'),
                  dst_file_type='csv',
                  dst_path=path_out)

    convert_files(file_lst=list_files(path_in, 'pickle'),
                  dst_file_type='json',
                  dst_path=path_out)
    convert_files(file_lst=list_files(path_in, 'json'),
                  dst_file_type='bin',
                  dst_path=path_out)
    convert_files(file_lst=list_files(path_in, 'csv'),
                  dst_file_type='bin',
                  dst_path=path_out)


if __name__ == '__main__':
    main()
