__all__ = ['checker']

from datetime import date
from sys import argv
# import re

_LEAP_DIVISOR = 4
_EXCLUDE = 100
_INCLUDE = 400


def _leap_year_check(a_year: int) -> bool:
    """leap year check"""
    if a_year % _EXCLUDE == 0 and a_year % _INCLUDE == 0:
        return True
    if a_year % _LEAP_DIVISOR == 0:
        return a_year % _EXCLUDE != 0


def checker(date_in: str) -> bool:
    """
    функция получает на вход дату в формате DD.MM.YYYY
    :param date_in: str
    :return: bool
    """
    if len(date_in := date_in.split('.')) != 3:
        return False
    date_in = [*map(int, date_in)][::-1]
    if date_in[1] > 31 or (date_in[1] == 2 and
                           date_in[0] == 29 and
                           not _leap_year_check(date_in[2])):
        return False
    try:
        date(*date_in)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    print("Not for separate use")
    # pattern = re.compile("\\d{1,2}\\.\\d{1,2}\\.\\d{4}")
    # if not argv:
    #     print("Date not found")
    # else:
    #     for item in argv[1:]:
    #         if pattern.match(item):
    #             print("The date is right indeed" if checker(item) else "The date is NOT right indeed")
    #             break
    #     else:
    #         print("Date not found")
