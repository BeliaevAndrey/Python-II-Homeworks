from homework_13.task_02.last_works import Rectangle
from homework_13.task_02.custom_exceptions import (RectangleTypeError, RectangleValueError)


class RectangleWorks:
    @classmethod
    def rectangle_create(cls, length: [int, float], width: [int, float]) -> Rectangle:
        if not isinstance(length, (int, float)):
            raise RectangleValueError(value=length)
        if not isinstance(width, (int, float)):
            raise RectangleValueError(value=width)
        if width <= 0 or length <= 0:
            raise RectangleValueError
        return Rectangle(length, width)

    @classmethod
    def rectangle_sum(cls, left: Rectangle, right: Rectangle) -> Rectangle:
        if not isinstance(left, Rectangle):
            raise RectangleTypeError(left)
        if not isinstance(right, Rectangle):
            raise RectangleTypeError(right)
        return left + right

    @classmethod
    def rectangle_sub(cls, left: Rectangle, right: Rectangle) -> Rectangle:
        if not isinstance(left, Rectangle):
            raise RectangleTypeError(left)
        if not isinstance(right, Rectangle):
            raise RectangleTypeError(right)
        return left - right
