__all__ = ['checker', 'argv']

from sys import argv

_LEAP_DIVISOR = 4
_EXCLUDE = 100
_INCLUDE = 400
_MONTH_DAYS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def _leap_year_check(a_year: int) -> bool:
    """leap year check"""
    if a_year % _EXCLUDE == 0 and a_year % _INCLUDE == 0:
        return True
    if a_year % _LEAP_DIVISOR == 0:
        return a_year % _EXCLUDE != 0
    return False


def checker(date_in: str) -> bool:
    """
    функция получает на вход дату в формате DD.MM.YYYY
    :param date_in: str
    :return: bool
    """
    if len(date_in := date_in.split('.')) != 3:
        return False
    if not all(map(lambda x: x.isdigit(), date_in)):
        return False
    date_in = [*map(int, date_in)]
    if date_in[0] < 1 or date_in[1] > len(_MONTH_DAYS) or date_in[1] <= 0:
        return False
    if date_in[1] == 2 and _leap_year_check(date_in[2]) and date_in[0] <= 29:
        return True
    elif date_in[0] > _MONTH_DAYS[date_in[1] - 1]:
        return False
    return True


if __name__ == '__main__':
    print("Not for separate use")
