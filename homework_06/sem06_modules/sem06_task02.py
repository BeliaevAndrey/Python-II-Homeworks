# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
from random import randint as r_int

__all__ = ['guess']


def guess(low: int, hi: int, attempts: int) -> bool:
    number = r_int(low, hi)
    count: int = 0
    while count < attempts:
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
