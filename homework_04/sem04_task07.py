# Функция получает на вход словарь с названием компании в качестве ключа и
# списком с доходами и расходами (3-10 чисел) в качестве значения.
# Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
from decimal import Decimal


def function(totals_dct: dict[str, list[float]]) -> bool:
    totals_dct = {company: list(map(Decimal, profit)) for
                  company, profit in
                  totals_dct.items()}

    return all(fin_value > 0 for fin_value
               in map(lambda company_profit:
                      sum(company_profit),
                      totals_dct.values()))


def main():
    companies_dct_false = {
        'first':   [1.0, -2.0, 3.0, ],
        'second':  [1.0, -2.0, 3.0, -4.0, ],
        'third':   [1.0, -2.0, 3.0, -4.0, 5.0, ],
        'fourth':  [1.0, -2.0, 3.0, -4.0, 5.0, -6.0, ],
        'fifth':   [1.0, -2.0, 3.0, -4.0, 5.0, -6.0, 7.0, ],
        'sixth':   [1.0, -2.0, 3.0, -4.0, 5.0, -6.0, 7.0, -8.0, ],
        'seventh': [1.0, -2.0, 3.0, -4.0, 5.0, -6.0, 7.0, -8.0, 9.0, ],
    }
    print(function(companies_dct_false))

    companies_dct_true = {
        'first':   [1.0, -2.0, 3.0, ],
        'second':  [1.0, -2.0, 3.0, 4.0, ],
        'third':   [1.0, -2.0, 3.0, -4.0, 5.0, ],
        'fourth':  [1.0, -2.0, 3.0, -4.0, 5.0, 6.0, ],
        'fifth':   [1.0, -2.0, 3.0, -4.0, 5.0, 6.0, 7.0, ],
        'sixth':   [1.0, -2.0, 3.0, -4.0, 5.0, 6.0, 7.0, 8.0, ],
        'seventh': [1.0, -2.0, 3.0, -4.0, 5.0, 6.0, 7.0, 8.0, 9.0, ],
    }
    print(function(companies_dct_true))

    companies_dct_false2 = {
        'first':   [0.1, -0.1, 0.3, ],
        'second':  [0.1, -0.1, 0.3, -0.11, ],
        'third':   [0.1, -0.1, 0.3, -0.11, 0.15, ],
        'fourth':  [0.1, -0.1, 0.3, -0.11, -0.15, -0.01, ],
        'fifth':   [0.1, -0.1, 0.3, -0.11, -0.15, -0.01, 0.12, ],
        'sixth':   [0.1, -0.1, 0.3, -0.11, -0.15, 0.01, -0.12, 0.005, ],
        'seventh': [0.1, -0.1, 0.3, -0.11, -0.15, 0.01, 0.12, -0.005, 0.011, ],
    }
    print(function(companies_dct_false2))


if __name__ == '__main__':
    main()
