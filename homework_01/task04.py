# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна
# подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа
# используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000


def find_number():
    comp_num = randint(LOWER_LIMIT, UPPER_LIMIT)
    user_num = int(input(f'Чтобы угадать число есть 10 попыток. '
                         f'\nВведите целое число в диапазоне {LOWER_LIMIT} - {UPPER_LIMIT}: '))
    counter = 9
    while counter > 0:
        if user_num < comp_num:
            print(f'{user_num} меньше загаданного числа')
        elif user_num > comp_num:
            print(f'{user_num} больше загаданного числа')
        elif user_num == comp_num:
            print(f'{user_num} = {comp_num} Угадано!')
            break
        user_num = int(input(f'осталось {counter} попыток. \nВведите целое число: '))
        counter -= 1
    else:
        print('Попытки закончились')


def main():
    find_number()


if __name__ == '__main__':
    main()
