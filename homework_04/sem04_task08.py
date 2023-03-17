# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


def function(**kwargs) -> dict:
    result = {}
    for name, value in kwargs.items():
        if name.endswith('s') and len(name) > 1:
            result[name.rstrip('s')] = None
        else:
            result[name] = value
    return result


def victim() -> tuple[dict, dict]:
    _01_s = 1
    _02_ = 2
    _03_s = 3
    _04_ = 4
    _05_s = 5
    _06_ = 6
    s = 7

    before = locals().copy()

    for var in function(**locals()).items():
        if var[0] not in locals().keys():
            locals()[var[0]] = var[1]

    after = locals().copy()
    return before, after


def main():
    result = victim()
    print(f'before: {result[0]}\n')
    print(f'after:  {result[1]}\n')


if __name__ == '__main__':
    main()
