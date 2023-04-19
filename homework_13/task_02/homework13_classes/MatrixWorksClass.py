from homework_13.task_02.last_works import Matrix
from homework_13.task_02.custom_exceptions import (MatrixMultiplyError,
                                                   MatrixTypeError,
                                                   MatrixValueError,
                                                   ConsistencyMatrixError)


class MatrixWorks:
    @classmethod
    def create_matrix(cls, in_list: list[list[int, float]]) -> Matrix:
        lengths = {len(row) for row in in_list}
        if len(lengths) > 1:
            raise ConsistencyMatrixError('rows')
        for row in in_list:
            for elem in row:
                if not isinstance(elem, (int, float)):
                    raise ConsistencyMatrixError('values')

        return Matrix(in_list)

    @classmethod
    def matrices_mul(cls, left: Matrix, right: [Matrix, int, float]) -> Matrix:
        if not isinstance(left, Matrix):
            raise MatrixTypeError(left)
        if not isinstance(right, (Matrix, int, float)):
            raise MatrixTypeError(right)
        if isinstance(right, Matrix) and left.cols != right.rows:
            raise MatrixMultiplyError
        return left * right

    @classmethod
    def matrices_sum(cls, left: Matrix, right: Matrix) -> Matrix:
        if not isinstance(left, Matrix):
            raise MatrixTypeError(left)
        if not isinstance(right, Matrix):
            raise MatrixTypeError(right)
        if left.rows != right.rows or left.cols != right.cols:
            raise MatrixValueError
        return left + right

