from typing import Callable, Any
import logging
from functools import wraps

FORMAT = "{asctime} - {msg}"

logging.basicConfig(filename='hw15_task01_error.log', filemode='a', format=FORMAT, style='{', level=logging.ERROR)
err_log = logging.getLogger()


def err_log_deco(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            err_log.error(f'Function {func.__name__} caused: {exc.__class__.__name__}: {exc}')
            return
    return wrapper


def main():
    err_log.info("mess2")


if __name__ == '__main__':
    main()
