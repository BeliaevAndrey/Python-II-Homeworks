# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.

class Archive:
    """A kind of singleton class"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Numbers and string are stored in two lists
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

    def __init__(self, number: int, a_string: str):
        """
        Init method
        :param number: int      -- some integer
        :param a_string: str    -- some string
        """
        self.number = number
        self.a_string = a_string

    def __str__(self):
        """User-readable representation method"""
        return (f'Number = {self.number}\nString={self.a_string}'
                f'\nNumbers = {self.numbers}'
                f'\nStrings = {self.strings}'
                )

    def __repr__(self):
        """String object representation method"""
        return f'Archive({self.number}, \'{self.a_string}\')'


def main():
    a = Archive(10, 'ten')
    b = Archive(11, 'eleven')
    c = Archive(12, 'twelve')

    print(f'{a}\n')
    print(f'{b}\n')
    print(f'{c}\n')
    
    print(f'{a=}\n')
    print(f'{b=}\n')
    print(f'{c=}\n')
    d = eval(repr(c))
    print(d)
    print(repr(d))


if __name__ == '__main__':
    main()
