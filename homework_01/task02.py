# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# * Дано a, b, c - стороны предполагаемого треугольника.
# * Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# * Если хотя бы в одном случае отрезок окажется больше суммы двух других,
#   то треугольника с такими сторонами не существует.
# * Отдельно сообщить является ли треугольник разносторонним,
#   равнобедренным или равносторонним.


def triangle(sides: tuple) -> None:
    for side in sides:
        if side >= sum(sides) - side:
            print("Треугольник не существует.")
            break
    else:
        if len(set(sides)) == 1:
            print('Треугольник равносторонний')
        elif len(set(sides)) == 3:
            print('Треугольник разносторонний')
        elif len(set(sides)) == 2:
            print('Треугольник равнобедренный')


def read() -> tuple:
    while True:
        try:
            a = float(input('Введите длину стороны a: '))
            b = float(input('Введите длину стороны b: '))
            c = float(input('Введите длину стороны c: '))
            return a, b, c
        except ValueError:
            print('Необходимо ввести целые или вещественные числа.')


def main():
    triangle(read())


if __name__ == '__main__':
    main()
