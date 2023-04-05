from typing import Callable, Any
from random import randint
import json
import os

__all__ = [
    'para_checker_dec',
    'dump_to_json_dec',
    'calls_amt_dec'
]

_RANGE_LO_LIM = 1
_RANGE_HI_LIM = 100
_ATMTS_LO_LIM = 1
_ATMTS_HI_LIM = 10


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


def dump_to_json_dec(file_name: str) -> Callable:
    def inner_dec(func: Callable) -> Callable:
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


def _read_json_para(filename: str) -> list[dict[str, dict[str]]]:
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r', encoding='utf-8') as f_in:
            parameters = json.load(f_in)
            parameters.append({})
    else:
        parameters = [{'args': {}, 'kwargs': {}, 'result': None}]
    return parameters


def _dump_json_para(filename: str,
                   parameters: list[dict[str, dict[str]]]) -> None:
    with open(filename, 'w', encoding='utf-8') as f_out:
        json.dump(parameters, f_out, indent=4)


def calls_amt_dec(count: int) -> Callable:
    def decorator2(func) -> Callable:
        counter = []

        def wrapper(*args, **kwargs) -> Any:
            for _ in range(count):
                res = func(*args, **kwargs)
                counter.append(res)
            return counter

        return wrapper

    return decorator2
