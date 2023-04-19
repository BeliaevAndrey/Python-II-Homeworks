import os
from last_works import Rectangle, FileLister, Matrix
from homework13_classes import RectangleWorks
from homework13_classes import MatrixWorks
from homework_13.task_02.custom_exceptions import *


class FileListerWorks:
    ...


def rectangle_part():
    rect_a = RectangleWorks.rectangle_create(100, 100)      # stub
    rect_b = RectangleWorks.rectangle_create(100, 100)      # stub

    try:
        rect_a = RectangleWorks.rectangle_create(11, -14)
    except RectangleValueError as exc:
        print(f'{exc.__class__.__name__}: {exc}')
    try:
        rect_b = RectangleWorks.rectangle_create(14, 'a')
    except RectangleValueError as exc:
        print(f'{exc.__class__.__name__}: {exc}')
    try:
        rect_e = RectangleWorks.rectangle_sum(rect_a, 10)
    except RectangleTypeError as exc:
        print(f'{exc.__class__.__name__}: {exc}')
    try:
        rect_e = RectangleWorks.rectangle_sub(rect_a, 'a')
    except RectangleTypeError as exc:
        print(f'{exc.__class__.__name__}: {exc}')
    rect_c = RectangleWorks.rectangle_sum(rect_a, rect_b)
    rect_d = RectangleWorks.rectangle_sub(rect_a, rect_b)
    print(rect_c)
    print(rect_d)


def matrix_part():
    mtx_a = MatrixWorks.create_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    mtx_b = MatrixWorks.create_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    mtx_d = MatrixWorks.create_matrix([[1, 2, 3, 4, ], [5, 6, 7, 8], [9, 10, 11, 12]])
    try:
        mtx_c = MatrixWorks.create_matrix([[10, 11, 12], [4, 5, 6, 100], [1, 2, 3], [7, 8, 9]])
    except ConsistencyMatrixError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')
    try:
        print(MatrixWorks.matrices_sum(mtx_a, mtx_d))
    except MatrixValueError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')
    try:
        print(MatrixWorks.matrices_mul(mtx_a, mtx_b))
    except MatrixMultiplyError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')
    try:
        print(MatrixWorks.matrices_mul(mtx_a, mtx_d))
    except MatrixMultiplyError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')
    try:
        print(MatrixWorks.matrices_mul(mtx_a, 10))
    except MatrixValueError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')
    try:
        print(MatrixWorks.matrices_mul(mtx_a, 'a'))
    except MatrixTypeError as exc:
        print(f'FAIL! {exc.__class__.__name__}: {exc}')


def main():
    # rectangle_part()
    matrix_part()


if __name__ == '__main__':
    main()
