from homework_14.task02.last_works import Matrix


def test_matrix():
    """
    >>> print(repr(Matrix([[1, 2, 3], [3, 2, 1], [4, 5, 6]])))
    Matrix([[1, 2, 3], [3, 2, 1], [4, 5, 6]])
    >>> print(repr(Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) * Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])))
    Matrix([[1, 8, 21, 40], [10, 30, 56, 88], [27, 60, 99, 144]])
    >>> print(repr(Matrix([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]]) + Matrix([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]])))
    Matrix([[2, 4, 6, 8], [8, 10, 12, 14], [16, 18, 20, 22]])
    >>> print(repr(Matrix([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]]) * 2))
    Matrix([[2, 4, 6, 8], [8, 10, 12, 14], [16, 18, 20, 22]])
    >>> Matrix([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]]) * '2'
    Traceback (most recent call last):
    ...
    homework_14.task02.custom_exceptions.MatrixExc.MatrixTypeError: AN ERROR OCCURRED. MatrixTypeError: 2 is not a 'Matrix' instance
    """
    ...


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
