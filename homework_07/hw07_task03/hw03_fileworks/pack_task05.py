"""
 Доработаем предыдущую задачу.
 Создайте новую функцию которая генерирует файлы с разными расширениями.
 Расширения и количество файлов функция принимает в качестве параметров.
 Количество переданных расширений может быть любым.
 Количество файлов для каждого расширения различно.
 Внутри используйте вызов функции из прошлой задачи.
"""
from random import randint as r_int
from .pack_task04 import creator

__all__ = ['creator_m']

MIN_FILES_AMT = 1
MAX_FILES_AMT = 42


def creator_m(extensions: [list[str], dict[str, int]]) -> None:
    """
    calls creator function from task04-module with certain extension
    :param extensions: list, dict -- list of extensions or dict of extensions and amount of files
    :return:
    """
    if isinstance(extensions, list):
        used_amt = set()
        for ext in extensions:
            amt = r_int(MIN_FILES_AMT, MAX_FILES_AMT)
            used_amt.add(amt)
            while amt in used_amt:
                amt = r_int(MIN_FILES_AMT, MAX_FILES_AMT)
            for _ in range(amt):
                creator(ext=ext, files_amt=amt)
                used_amt.add(amt)
    elif isinstance(extensions, dict):
        for i_ext, i_amt in extensions.items():
            creator(ext=i_ext, files_amt=i_amt)


if __name__ == '__main__':
    print('Not for separate use')
