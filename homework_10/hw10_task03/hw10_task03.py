# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных),
# которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.

from hw10_file_walker import FileLister
from hw10_csv_works import CsvWorks
from hw10_json_works import JsonWorks
from hw10_pickle_works import PickleWorks


def main():
    searcher = FileLister('/home/andrew/Documents/geekbrains/Python2023/Homeworks/homework_08/hw08_task02/tst_out')
    json_file_list = searcher.list_files('json', full_path=False)
    for ln in json_file_list:
        print(JsonWorks.json_reader(ln[0], ln[1]))
    csv_file_list = searcher.list_files('csv', full_path=False)
    for ln in csv_file_list:
        print(CsvWorks.csv_reader(ln[0], ln[1]))
    pickle_file_list = searcher.list_files('bin', full_path=False)
    for ln in pickle_file_list:
        print(PickleWorks.pickle_reader(ln[0], ln[1]))


if __name__ == '__main__':
    main()
