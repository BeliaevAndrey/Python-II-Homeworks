# Добавьте к задачам 1 и 2 строки документации для классов.
from time import time


class MyString(str):
    """Extends 'str'-class"""

    def __new__(cls, content: str, author: str) -> 'MyString':
        """
        Init method
        :param content: str -- string itself
        :param author:  str -- author copyright
        """
        instance = super().__new__(cls, content)
        instance.content = content
        instance.author = author
        instance.created = time()
        return instance

    def __str__(self) -> str:
        """User-readable representation method"""
        return self.content

    def __repr__(self) -> str:
        """User-readable representation method"""
        return f'MyString(\'{self.content}\', \'{self.author}\')'


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
    print(MyString.__doc__)
    print(Archive.__doc__)
    help(MyString)
    help(Archive)


if __name__ == '__main__':
    main()
