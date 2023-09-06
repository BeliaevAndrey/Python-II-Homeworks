import unittest

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


class TestMatrixClass(unittest.TestCase):

    def test_create_success(self):
        assert (NEW_MATRIX_SQR == Matrix([[1, 2, 3], [3, 2, 1], [4, 5, 6]]))

    def test_create_fail_common(self):
        self.assertRaises(ConsistencyMatrixError,
                          Matrix,
                          [[1, 2, 3], [3, 2, 1, 4], [4, 5, 6]])

    def test_eq_success(self):
        self.assertTrue(NEW_MATRIX_SQR == Matrix([[1, 2, 3], [3, 2, 1], [4, 5, 6]]))
        self.assertFalse(NEW_MATRIX_SQR == Matrix([[1, 2, 3], [3, 2, 4], [4, 5, 6]]))

    def test_ne_success(self):
        self.assertFalse(NEW_MATRIX_SQR != Matrix([[1, 2, 3], [3, 2, 1], [4, 5, 6]]))
        self.assertTrue(NEW_MATRIX_SQR != Matrix([[1, 2, 3], [3, 2, 4], [4, 5, 6]]))

    def test_eq_fail(self):
        self.assertRaises(MatrixTypeError,
                          NEW_MATRIX_RCT.__eq__,
                          [[1, 2, 3], [3, 2, 1, 4], [4, 5, 6]])

    def test_ne_fail(self):
        self.assertRaises(MatrixTypeError,
                          NEW_MATRIX_RCT.__ne__,
                          [[1, 2, 3], [3, 2, 1, 4], [4, 5, 6]])

    def test_matrix_mul_success(self):
        self.assertTrue(NEW_MATRIX_MUL_L * NEW_MATRIX_MUL_R == MATRIX_MUL_ANS)

    def test_matrix_mul_fail(self):
        self.assertRaises(MatrixMultiplyError,
                          NEW_MATRIX_MUL_L.__mul__,
                          NEW_MATRIX_SQR)


if __name__ == '__main__':
    unittest.main(verbosity=2)
