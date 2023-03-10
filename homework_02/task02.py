# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте
# для проверки своего результата.
HEX_CONST = 16
HEX_ALPHA = '0123456789ABCDEF'


def get_hex(num: int) -> str:
    out_string = ''
    while num:
        out_string = HEX_ALPHA[num % HEX_CONST] + out_string
        num //= HEX_CONST
    return '0x' + out_string


def read_int() -> int:
    while True:
        try:
            return int(input('Введите целое число: '))
        except TypeError:
            print('Требуется целое число.')


def main():
    number = read_int()
    number_hex = get_hex(number)
    print(f'\nЧисло {number:^20} {"в шестнадцатеричном представлении:":<30}{number_hex:>20}'
          f'\n{"Проверка функцией hex():":>61}{hex(number):>20}')
    print(f'{number_hex.lower() == hex(number)}'.rjust(81))


if __name__ == '__main__':
    main()
