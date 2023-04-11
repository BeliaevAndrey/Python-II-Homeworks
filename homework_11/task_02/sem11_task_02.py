# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра


class Archive:
    """A kind of singleton class"""
    _instance = None

    def __new__(cls, *args, **kwargs) -> 'Archive':
        """
        Here numbers and string are been placed in two lists
        :param args:
        :param kwargs:
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.numbers = []
            cls._instance.strings = []
        else:
            cls._instance.numbers.append(cls._instance.number)
            cls._instance.strings.append(cls._instance.a_string)
        return cls._instance

    def __init__(self, number: int, a_string: str) -> None:
        """
         Init method
         :param number: int      -- some integer
         :param a_string: str    -- some string
         """
        self.number = number
        self.a_string = a_string

    def __str__(self) -> str:
        """User-readable representation method"""
        return f'{self.number} {self.a_string}'

    def __repr__(self) -> str:
        """String object representation method"""
        return f'Archive({self.number}, {self.a_string})'


def main():
    a = Archive(10, 'ten')
    b = Archive(11, 'eleven')
    c = Archive(12, 'twelve')
    print(a)
    print(b)
    print(c)
    print(a.numbers)
    print(a.strings)
    print(b.numbers)
    print(b.strings)
    print(c.numbers)
    print(c.strings)


if __name__ == '__main__':
    main()
