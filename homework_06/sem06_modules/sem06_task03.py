# * Улучшаем задачу 2.
# * Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# * Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# * Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
from random import randint as r_int
from sys import argv

__all__ = ['guess_play']


def guess_play(lo: int, hi: int = 100, attempts_amt: int = 3) -> bool:
    number = r_int(lo, hi)
    count: int = 0
    while count < attempts_amt:
        count += 1
        print(f'attempt: {count}')
        guess_num = int(input('Enter integer: '))
        if guess_num == number:
            return True
        elif guess_num < number:
            print("Your number is lesser")
        else:
            print("Your number is greater")
    return False


if __name__ == '__main__':
    print("Not for separate use")
