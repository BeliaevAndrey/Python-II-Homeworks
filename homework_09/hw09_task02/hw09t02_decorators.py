from typing import Callable, Any
import csv
import os
import json
from functools import wraps

__all__ = [
    'starting_decor'
]


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
            parameters.append({})
    else:
        parameters = [{'args': {}, 'kwargs': {}, 'result': None}]
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

        @wraps(func)    # This allows a doc-string of function to be in reach.
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
    def inner_dec(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            parameters = _read_json_para(file_name)
            if args:
                parameters[-1]['args'] = {f'arg{i}': args[i] for i in range(len(args))}
            if kwargs:
                parameters[-1]['kwargs'] = kwargs
            result = func(*args, **kwargs)
            parameters[-1]['result'] = result
            _dump_json_para(file_name, parameters)
            return result

        return wrapper

    return inner_dec


