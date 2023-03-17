# 3. Напишите функцию принимающую на вход только ключевые параметры и возвращающую
# словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def function(**kwargs) -> dict:
    def hashed_key(an_arg) -> [int, str]:
        try:
            return hash(an_arg)
        except TypeError:
            return an_arg.__repr__()

    return {hashed_key(i_val): i_key for i_key, i_val in kwargs.items()}


def printer(dict_in: dict) -> None:
    for i_key, i_val in dict_in.items():
        print(f'{i_key:.<30} {i_val}')


def main():
    printer(function(a='a_cat',
                     b=2,
                     c={1, 2, 3},
                     d=4,
                     e=[4, 5, 6],
                     f={'a': 7, 'b': 8, 'c': 9},
                     g=('something', 123456),
                     h=map
                     ))


if __name__ == '__main__':
    main()
