# Создайте функцию генератор чисел Фибоначчи (см. Википедию)
def fibonacci_gen(limit_pos: int):
    fib = []
    yield from [(k := (0 if i == 0 else 1 if i < 3 else (fib[i-1] + fib[i-2])), fib.append(k))[0]
                for i in range(0, limit_pos)]


def main():
    print(*fibonacci_gen(50))


if __name__ == '__main__':
    main()
