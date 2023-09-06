# Создайте класс Матрица. Добавьте методы для:
#   * вывода на печать,
#   * сравнения,
#   * сложения,
#   * *умножения матриц

class Matrix:

    def __init__(self, a_matrix: list[list[int, float]]) -> None:
        if not self.check(a_matrix):
            raise ValueError("Matrix of wrong dimensions")
        self._rows = len(a_matrix)
        self._cols = len(a_matrix[0])
        self._matrix = a_matrix

    @staticmethod
    def check(a_matrix):
        for row in a_matrix:
            if len(row) != len(a_matrix[0]):
                return False
        return True

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Not a matrix type!")
        if self._rows != other._rows or self._cols != other._cols:
            raise ValueError("Matrices are to be equal dimensions")
        new_matrix = [[0] * self._cols for _ in range(self._rows)]
        for i in range(self._rows):
            for j in range(self._cols):
                new_matrix[i][j] = self._matrix[i][j] + other._matrix[i][j]
        return Matrix(new_matrix)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        if self._rows != other._rows or self._cols != other._cols:
            return False
        for i in range(self._rows):
            for j in range(self._cols):
                if self._matrix[i][j] != other._matrix[i][j]:
                    return False
        return True

    def __mul__(self, other):
        """
        Calculates a multiplication of matrices or multiplication the matrix by a number
        :param other: [int, float, Matrix]    -- other Matrix object
        :return: Matrix                       -- new Matrix object
        """
        if isinstance(other, Matrix):
            return self.__rmul__(other)
        if isinstance(other, (int, float)):
            new_matrix = [[0] * self._cols for _ in range(self._rows)]
            for i in range(self._rows):
                for j in range(self._cols):
                    new_matrix[i][j] = self._matrix[i][j] * other
            return Matrix(new_matrix)
        else:
            raise TypeError("Unsupported type of operand")

    def __rmul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Not a matrix type!")
        if self._cols != other._rows:
            raise ValueError("Matrices rows amt is to be equal other matrix cols amt")
        new_matrix = [[0] * other._cols for _ in range(self._rows)]
        for i in range(self._rows):
            for j in range(other._cols):
                for k in range(other._rows):
                    new_matrix[i][j] += self._matrix[i][k] * other._matrix[k][j]
        # new_matrix = [[sum([self._matrix[i][k] * other._matrix[k][j]
        #                     for k in range(other._rows)])
        #               for j in range(other._cols)]
        #               for i in range(self._rows)]
        return Matrix(new_matrix)

    def __str__(self):
        return '\n'.join(''.join([f'{x:^5}' for x in row]) for row in self._matrix) + '\n'

    def __repr__(self):
        """String object representation method"""
        return f'Matrix({self._matrix})'


def main():
    mtx_a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    mtx_b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    mtx_c = Matrix([[10, 11, 12], [4, 5, 6], [1, 2, 3], [7, 8, 9]])
    mtx_d = Matrix([[1, 2, 3, 4, ], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(repr(mtx_a))
    print(mtx_a)
    print(mtx_b)
    print(mtx_c)
    print(mtx_d)

    print(f'{mtx_a == mtx_b=}')
    print(f'{mtx_a == mtx_b=}')
    print(f'{mtx_b == mtx_c=}')
    print(f'{mtx_b != mtx_c=}')
    print(f'{mtx_c != mtx_d=}')
    print(mtx_a + mtx_b)
    print(mtx_a + mtx_c)
    try:
        print(mtx_c + mtx_d)
    except ValueError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')
    try:
        print(mtx_a * mtx_b)
    except ValueError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')
    try:
        print(mtx_a * mtx_d)
    except ValueError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')
    try:
        print(mtx_a * 10)
    except TypeError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')


if __name__ == '__main__':
    main()
