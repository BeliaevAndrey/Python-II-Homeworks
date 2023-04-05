from typing import Callable, Any
from random import randint
import csv
import os
import json
from functools import wraps

__all__ = [
    'starting_decor',
    'dump_to_json_dec',
    'para_checker_dec',
]

_RANGE_LO_LIM = 1
_RANGE_HI_LIM = 100
_ATMTS_LO_LIM = 1
_ATMTS_HI_LIM = 10


# Common csv- and json-files read/write functions section
def _read_csv_rand_nums(file_name: str) -> list[list[str, int]]:
    """csv-file read-to-list function """
    coefficients = []
    with open(file_name, 'r', encoding='utf-8') as f_in:
        read_csv = csv.reader(f_in, dialect='excel', delimiter=';')
        coefficients.append(next(read_csv))
        for row in read_csv:
            coefficients.append([int(row[0])] + [*map(float, row[1:])])
            # print("SRC: ", row)

    return coefficients


def _read_json_para(filename: str) -> list[dict[str, dict[str]]]:
    """ json-file read-to-list-of-dicts function """
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r', encoding='utf-8') as f_in:
            parameters = json.load(f_in)
    else:
        parameters = []
    return parameters


def _dump_json_para(filename: str,
                    parameters: list[dict[str, dict[str]]]) -> None:
    """ json-file dump function """
    with open(filename, 'w', encoding='utf-8') as f_out:
        json.dump(parameters, f_out, indent=4)


# Decorators section
def starting_decor(file_name: str) -> Callable:
    """Starts wrapper of calculating function"""

    def inner(func: Callable) -> Callable:

        @wraps(func)  # This allows a doc-string of "func" to be in reach.
        def wrapper(*args) -> Any:
            """
            Calls calculating function once if args are,
            otherwise as many times as many rows in a list obtained.
            """
            if args:
                return func(*args)
            a_table: list[list[str, int]] = _read_csv_rand_nums(file_name)
            a_table[0].append('Result')
            for i in range(1, len(a_table)):
                a_table[i].append(func(*a_table[i][1:]))
                # print(a_table[i])

            return a_table

        return wrapper

    return inner


def dump_to_json_dec(file_name: str) -> Callable:
    """
    Decorating function, dumps a parameters and results dictionary to a json-file.
    Warning: file is updated, not rewritten.
    """

    def inner_dec(func: Callable) -> Callable:
        param_res = []  # caching list
        call_count = 0  # accumulates call amt

        @wraps(func)
        def wrapper(*args) -> Any:
            nonlocal call_count
            nonlocal param_res
            call_count += 1
            if not param_res:
                param_res = _read_json_para(file_name)
            param_res.append({'args': {'No': call_count,
                                       'a': args[0],
                                       'b': args[1],
                                       'c': args[2],
                                       }})
            result = func(*args)
            param_res[-1]['result'] = result
            _dump_json_para(file_name, param_res)
            return result

        return wrapper

    return inner_dec


def para_checker_dec(func: Callable) -> Callable:
    range_lim = [*range(_RANGE_LO_LIM, _RANGE_HI_LIM)]
    attempts_amt_lim = [*range(_ATMTS_LO_LIM, _ATMTS_HI_LIM + 1)]

    def wrapper(num_sc, attempts):
        if num_sc not in range_lim:
            num_sc = randint(_RANGE_LO_LIM, _RANGE_HI_LIM)
        if attempts not in attempts_amt_lim:
            attempts = randint(_ATMTS_LO_LIM, _ATMTS_HI_LIM)
        func(num_sc, attempts)

    return wrapper

