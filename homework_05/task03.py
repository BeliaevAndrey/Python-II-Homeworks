# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой
# длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии
from decimal import Decimal


def gen_dic(name_lst: list[str],
            salary_lst: list[int],
            award_lst: list[str],
            ) -> dict[str, float]:
    return {name: float(salary * award) for
            name, salary, award in
            zip(name_lst,
                map(Decimal, salary_lst),
                list(map(lambda x: Decimal(x.replace('%', '')) / 100, award_lst)))
            }


def main() -> None:
    name_lst: list[str] = ['First', 'Second', 'Third']
    salary_lst: list[int] = [120_000, 100_000, 140_000]
    award_lst: list[str] = ['10.25%', '7.75%', '8.95%']
    print('\n'.join(f'{item[0]:.<10}{item[1]:.>15.2f}'
                    for item in gen_dic(name_lst, salary_lst, award_lst).items()))


if __name__ == '__main__':
    main()
