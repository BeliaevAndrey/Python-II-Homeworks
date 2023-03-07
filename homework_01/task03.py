# Напишите код, который запрашивает число и сообщает, является ли оно простым или
# составным. Используйте правило для проверки: “Число является простым, если
# делится нацело только на единицу и на себя”. Сделайте ограничение на ввод
# отрицательных чисел и чисел больше 100 тысяч.

def is_simple(num: int) -> bool:
    if num < 2 or num % 2 == 0:
        return False
    if num == 2:
        return True
    limit = int(num ** 0.5) + 1
    for i in range(3, limit, 2):
        if not num % i:
            return False
    return True


def main():
    while True:
        number = input('Введите целое число для проверки'
                       '\nв диапазоне 0 - 100 000'
                       '\n(или exit для выхода):\n'
                       '_> ')
        if number.strip().lower() == 'exit':
            break
        try:
            number = int(number)
        except ValueError:
            print('Требуется целое число.')
        if number < 0 or number > 1e5:
            print('Требуется число в диапазоне 0 - 100 000.')
        else:
            if is_simple(number):
                print(f'{number} -- простое')
            else:
                print(f'{number} -- составное')


def test():
    for j in range(int(1e5)):
        if is_simple(j):
            print(j, "prime")


if __name__ == '__main__':
    # main()
    test()
