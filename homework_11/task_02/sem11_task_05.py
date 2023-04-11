# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину.
# При вычитании не допускайте отрицательных значений.
class Rectangle:

    def __init__(self, width: float, length: float = None) -> None:
        """
        Init method
        :param width: float     -- rectangle width
        :param length: float    -- rectangle height
        """
        self.width = width
        self.length = length if length else width

    def get_perimeter(self) -> float:
        """Calculates and returns a perimeter of object"""
        return 2 * (self.width + self.length)

    def get_area(self) -> float:
        """Calculates and returns an area of object"""
        return self.width * self.length

    def __add__(self, other) -> 'Rectangle':
        """
        Calculates and returns a new object based on
        sum of self perimeter and a one of another
        :param other: Rectangle     -- a Rectangle object to add
        :return: Rectangle          -- a new Rectangle object
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Rectangle' instance")
        ratio_width = self.width / self.get_perimeter()
        ratio_length = self.length / self.get_perimeter()
        new_perimeter = self.get_perimeter() + other.get_perimeter()
        return Rectangle(new_perimeter * ratio_width, new_perimeter * ratio_length)

    def __sub__(self, other) -> 'Rectangle':
        """
        Calculates and returns a new object based on
        subtraction of self perimeter and a one of another
        :param other: Rectangle     -- a Rectangle object to add
        :return: Rectangle          -- a new Rectangle object
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Rectangle' instance")
        ratio_width = self.width / self.get_perimeter()
        ratio_length = self.length / self.get_perimeter()
        new_perimeter = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(new_perimeter * ratio_width, new_perimeter * ratio_length)

    def __str__(self) -> str:
        """User-readable representation method"""
        return (f'\nRectangle:\n{self.width} X {self.length}'
                f'\nPerimeter: {self.get_perimeter()}'
                f'\nArea:      {self.get_area()}')

    def __repr__(self) -> str:
        """String object representation method"""
        return f'Rectangle({self.width}, {self.length})'


def main():
    rect_a = Rectangle(10, 20)
    rect_b = Rectangle(14, 7)
    rect_c = rect_a + rect_b
    print(rect_c)
    print(rect_a)
    print(rect_b)


if __name__ == '__main__':
    main()
