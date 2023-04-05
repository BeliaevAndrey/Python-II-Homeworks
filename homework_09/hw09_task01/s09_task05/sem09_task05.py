# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
#   - декораторами для сохранения параметров,
#   - декоратором контроля значений и
#   - декоратором для многократного запуска.
# Выберите верный порядок декораторов.
from s09t05_decors import para_checker_dec, dump_to_json_dec, calls_amt_dec


@calls_amt_dec(3)
@para_checker_dec
@dump_to_json_dec('para_log.json')
def guess(num_sc, attempts) -> str:
    result = 'Have not result yet'
    while attempts:
        print(f'left {attempts} attempts.', end=' ')
        attempts -= 1
        num = int(input('Input a number: '))
        if num == num_sc:
            print(f'Number found: {num}')
            break
        else:
            advice = ['lesser', 'greater']
            print(result := f'Your number is {advice[num > num_sc]} then right')
    else:
        print(result := f'You loose. Right number is {num_sc}')
    return result


def main():
    guess(80, 5)


if __name__ == '__main__':
    main()
