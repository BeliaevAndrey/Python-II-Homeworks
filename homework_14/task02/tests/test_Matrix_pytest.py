import pytest

from homework_14.task02.last_works import Matrix
from homework_14.task02.custom_exceptions import (ConsistencyMatrixError,
                                                  MatrixMultiplyError,
                                                  MatrixTypeError,
                                                  MatrixValueError)

NEW_MATRIX_SQR = Matrix([[1, 2, 3], [3, 2, 1], [4, 5, 6]])
NEW_MATRIX_SQR_MUL_TEN_ANS = Matrix([[10, 20, 30], [30, 20, 10], [40, 50, 60]])
NEW_MATRIX_RCT = Matrix([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]])
NEW_MATRIX_MUL_L = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
NEW_MATRIX_MUL_R = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
MATRIX_MUL_ANS = Matrix([[70, 80, 90], [158, 184, 210], [246, 288, 330]])
MATRIX_RCT_SUM_ANS = Matrix([[2, 4, 6, 8], [8, 10, 12, 14], [16, 18, 20, 22]])


@pytest.mark.parametrize('expected, actual', [
    (NEW_MATRIX_SQR, [[1, 2, 3], [3, 2, 1], [4, 5, 6]]),
    (NEW_MATRIX_RCT, [[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]]), ])
def test_create_success(expected, actual):
    assert (expected == Matrix(actual))
    assert (id(expected) != id(Matrix(actual)))


@pytest.mark.parametrize('fail_matrix, expected_exc', [
    ([[1, 2, 3], [3, 2, 1], [4, 5, 'a']], ConsistencyMatrixError),
    ([[1, 2, 3, 4], [4, 5, 6], [8, 9, 10, 11]], ConsistencyMatrixError)])
def test_create_fail_common(fail_matrix, expected_exc):
    with pytest.raises(expected_exc):
        Matrix(fail_matrix)


@pytest.mark.parametrize('fail_matrix, expected_exc', [
    ([[1, 2, 3], [3, 2, 1], [4, 5, 'a']], ConsistencyMatrixError), ])
def test_create_fail_values(fail_matrix, expected_exc):
    with pytest.raises(expected_exc, match="AN ERROR OCCURRED. "
                                           "Inconsistent Matrix Error: "
                                           "All values must be of types 'int' or 'float'"):
        Matrix(fail_matrix)


@pytest.mark.parametrize('fail_matrix, expected_exc', [
    ([[1, 2, 3, 4], [4, 5, 6], [8, 9, 10, 11]], ConsistencyMatrixError)])
def test_create_fail_rows(fail_matrix, expected_exc):
    with pytest.raises(expected_exc, match="AN ERROR OCCURRED. "
                                           "Inconsistent Matrix Error: "
                                           "All rows must be of same length"):
        Matrix(fail_matrix)


@pytest.mark.parametrize('matrix_left, matrix_right, expected', [
    (NEW_MATRIX_MUL_L, NEW_MATRIX_MUL_R, MATRIX_MUL_ANS)
])
def test_matrix_mul_success(matrix_left, matrix_right, expected):
    assert (matrix_left * matrix_right == expected)


@pytest.mark.parametrize('matrix_left, matrix_right, expected_exception', [
    (NEW_MATRIX_MUL_R, NEW_MATRIX_MUL_R, MatrixMultiplyError)
])
def test_matrix_mul_fail(matrix_left, matrix_right, expected_exception):
    with pytest.raises(expected_exception,
                       match="AN ERROR OCCURRED. "
                             "MatrixMultiplyError: "
                             "Operation not permitted if rows amount of first matrix "
                             "is not equal to columns amount of other one"):
        matrix_left * matrix_right


@pytest.mark.parametrize('matrix_left, number, expected', [
    (NEW_MATRIX_SQR, 10, NEW_MATRIX_SQR_MUL_TEN_ANS)
])
def test_matrix_mul_by_num_success(matrix_left, number, expected):
    assert (matrix_left * number == expected)


@pytest.mark.parametrize('matrix_left, number, expected_exception', [
    (NEW_MATRIX_SQR, '10', MatrixTypeError)
])
def test_matrix_mul_by_num_fail(matrix_left, number, expected_exception):
    with pytest.raises(expected_exception, match="AN ERROR OCCURRED. "
                                                 "MatrixTypeError: "
                                                 f"{number} is not a 'Matrix' instance"):
        matrix_left * number


@pytest.mark.parametrize('matrix_left, matrix_right, expected', [
    (NEW_MATRIX_RCT, NEW_MATRIX_RCT, MATRIX_RCT_SUM_ANS)
])
def test_matrix_sum_success(matrix_left, matrix_right, expected):
    assert ((tmp := matrix_left + matrix_right) == expected)
    assert (id(tmp) != id(expected))


@pytest.mark.parametrize('matrix_left, matrix_right, expected_exception', [
    (NEW_MATRIX_RCT, NEW_MATRIX_SQR, MatrixValueError)
])
def test_matrix_sum_fail(matrix_left, matrix_right, expected_exception):
    with pytest.raises(expected_exception,
                       match="AN ERROR OCCURRED. "
                             "MatrixValueError: "
                             "Operation not permitted for different-dimensional matrices"):
        matrix_left + matrix_right


if __name__ == '__main__':
    pytest.main(['-v'])
