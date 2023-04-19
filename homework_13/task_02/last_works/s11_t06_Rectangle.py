# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения
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
        # if not isinstance(other, self.__class__):         This condition is checked externally
        #     raise TypeError("Not a 'Rectangle' instance")
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
        # if not isinstance(other, self.__class__):         This condition is checked externally
        #     raise TypeError("Not a 'Rectangle' instance")
        ratio_width = self.width / self.get_perimeter()
        ratio_length = self.length / self.get_perimeter()
        new_perimeter = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(new_perimeter * ratio_width, new_perimeter * ratio_length)

    def __str__(self) -> str:
        """User-readable representation method"""
        return (f'\nRectangle: {round(self.width, 3)} X {round(self.length, 3)}'
                f'\nPerimeter: {round(self.get_perimeter(), 3)}'
                f'\nArea:      {round(self.get_area(), 3)}')

    def __repr__(self) -> str:
        """String object representation method"""
        return f'Rectangle({self.width}, {self.length})'

    # Type-checks in methods below left untouched in attempt
    # to keep consistency of standard methods
    def __eq__(self, other) -> bool:
        """Override of 'equals' method"""
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Rectangle' instance")
        return self.get_area() is other.get_area()

    def __ne__(self, other):
        """Override of 'not equals' method"""
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Rectangle' instance")
        return self.get_area() is not other.get_area()

    def __lt__(self, other):
        """Override of 'lesser than' method"""
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Rectangle' instance")
        return self.get_area() < other.get_area()

    def __gt__(self, other):
        """Override of 'greater than' method"""
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Rectangle' instance")
        return self.get_area() > other.get_area()

    def __le__(self, other):
        """Override of 'lesser or equals' method"""
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Rectangle' instance")
        return self.get_area() <= other.get_area()

    def __ge__(self, other):
        """Override of 'greater or equals' method"""
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Rectangle' instance")
        return self.get_area() >= other.get_area()


if __name__ == '__main__':
    print('Now it\'s a module')
