# Напишите функцию для транспонирования матрицы

def transpose2(matrix: list[list[int]]) -> list[list[int]]:
    return list(map(list, zip(*matrix)))


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """
    Транспонирование — в линейной алгебре это операция над матрицами
    в результате которой матрица поворачивается относительно своей главной диагонали.
    При этом столбцы исходной матрицы становятся строками результирующей.
    :param matrix: list[list[int]] incoming matrix
    :return: list[list[int]] transposed matrix
    """
    temp = []
    for i in range(len(matrix[0])):
        temp.append([])
        for j in range(len(matrix)):
            temp[i].append(matrix[j][i])
    return temp


def filler(width: int,
           height: int) -> list[list[int]]:
    """
    Filling a test matrix
    :param width: int   -- amount of elements in row
    :param height: int  -- amount of rows
    :return: list[list[int]]:   -- filled matrix
    """
    new_matrix = [[] for _ in range(height)]
    for row in range(height):
        for element in range(width):
            new_matrix[row].append(row * width + element + 1)
    return new_matrix


def printer(matrix: list[list]) -> None:
    print('\n'.join(''.join(f'{str(c):>4}' for c in s) for s in matrix))
    print('====' * len(matrix[0]))


def main():
    print(f'{" FIRST ":*^80}')
    test_matrix = filler(2, 4)
    printer(test_matrix)
    printer(transpose(test_matrix))
    printer(transpose2(test_matrix))
    test_matrix = filler(20, 10)
    print(f'{" SECOND ":*^80}')
    printer(test_matrix)
    printer(transpose(test_matrix))
    printer(transpose2(test_matrix))


if __name__ == '__main__':
    main()
