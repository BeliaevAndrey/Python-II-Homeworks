# Напишите код, который запрашивает число и сообщает, является ли оно простым или
# составным. Используйте правило для проверки: “Число является простым, если
# делится нацело только на единицу и на себя”. Сделайте ограничение на ввод
# отрицательных чисел и чисел больше 100 тысяч.

def is_simple(num: int) -> bool:
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    limit = int(num ** 0.5) + 1
    for i in range(3, limit, 2):
        if not num % i:
            return False
    return True


def main():
    while True:
        number = input('Введите целое число для проверки'
                       '\nв диапазоне 2 - 100 000'
                       '\n(или exit для выхода):\n'
                       '_> ')
        if number.strip().lower() == 'exit':
            break
        try:
            number = int(number)
        except ValueError:
            print('Требуется целое число.')
        if number < 2 or number > 1e5:      # единицу н относят к простым числам
            print('Требуется число в диапазоне 2 - 100 000.')
        else:
            if is_simple(number):
                print(f'{number} -- простое\n')
            else:
                print(f'{number} -- составное\n')


if __name__ == '__main__':
    main()
