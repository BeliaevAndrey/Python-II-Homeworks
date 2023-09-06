from homework_14.task02.custom_exceptions import (MatrixValueError,
                                                  MatrixTypeError,
                                                  ConsistencyMatrixError,
                                                  MatrixMultiplyError)


class Matrix:
    _rows: int = None
    _cols: int = None
    _a_matrix: list[list[int, float]] = None

    def __init__(self, a_matrix: list[list[int, float]]) -> None:
        """
        Init matrix
        :param cols: int    -- a number of columns
        :param rows: int    -- a number of rows
        """
        self.consistency_check(a_matrix)
        self._rows = len(a_matrix)
        self._cols = len(a_matrix[0])
        self._a_matrix = a_matrix

    @staticmethod
    def consistency_check(a_matrix: list[list[int, float]]) -> None:
        """
        Checks if matrix rows are of same length.
        Checks if all values are of appropriate type.
        :param a_matrix: list[list[int, float]]     -- a matrix to validate
        :return: None
        """
        for row in a_matrix[1:]:
            if len(row) != len(a_matrix[0]):
                raise ConsistencyMatrixError('rows')
        for row in a_matrix:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise ConsistencyMatrixError('values')

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    @property
    def a_matrix(self):
        return self._a_matrix

    def __add__(self, other) -> 'Matrix':
        """
        Calculates a sum of matrices
        :param other: Matrix    -- other Matrix object
        :return: Matrix         -- new Matrix object
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Matrix'-type object")
        if self._rows != other._rows or self._cols != other._cols:
            raise MatrixValueError
        new_matrix = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        for j in range(self._rows):
            for i in range(self._cols):
                new_matrix[j][i] = self._a_matrix[j][i] + other._a_matrix[j][i]
        return Matrix(new_matrix)

    def __mul__(self, other) -> 'Matrix':
        """
        Calculates a multiplication of matrices or multiplication the matrix by a number
        :param other: [int, float, Matrix]    -- other Matrix object
        :return: Matrix                       -- new Matrix object
        """
        if isinstance(other, self.__class__):
            return self.__rmul__(other)
        elif isinstance(other, int) or isinstance(other, float):
            new_matrix = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
            for j in range(self._rows):
                for i in range(self._cols):
                    new_matrix[j][i] = self.a_matrix[j][i] * other
            return Matrix(new_matrix)
        else:
            raise MatrixTypeError(other)

    def __rmul__(self, other) -> 'Matrix':
        """
        Calculates a multiplication of matrices
        :param other: Matrix    -- other Matrix object
        :return: Matrix         -- new Matrix object
        """
        if not isinstance(other, self.__class__):
            raise MatrixTypeError(other)
        if self._cols != other._rows:
            raise MatrixMultiplyError
        new_matrix = [[0] * other._cols for _ in range(self._rows)]
        for i in range(self._rows):
            for j in range(other._cols):
                for k in range(other._rows):
                    new_matrix[i][j] += self._a_matrix[i][k] * other._a_matrix[k][j]
        return Matrix(new_matrix)

    def __eq__(self, other) -> bool:
        """Returns True if the matrix equals to other one"""
        if self is other:
            return True
        if not isinstance(other, self.__class__):
            raise MatrixTypeError(other)
        if self._rows != other._rows or self._cols != other._cols:
            return False
        for j in range(self._rows):
            for i in range(self._cols):
                if self._a_matrix[j][i] != other._a_matrix[j][i]:
                    return False
        return True

    def __ne__(self, other) -> bool:
        """Returns True if the matrix not equals to other"""
        return not self.__eq__(other)

    def __str__(self) -> str:
        """User-readable representation method"""
        return '\n'.join(['\t'.join(map(str, row)) for row in self._a_matrix]) + '\n'

    def __repr__(self):
        """String object representation method"""
        return f'Matrix({self._a_matrix})'


if __name__ == '__main__':
    # print('Now it\'s a module')
    print(repr(Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) * Matrix(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])))
