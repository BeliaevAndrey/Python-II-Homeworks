# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)
from time import time


class MyString(str):
    """Extends 'str'-class"""

    def __new__(cls, content: str, author: str) -> 'MyString':
        instance = super().__new__(cls, content)
        instance.content = content
        instance.author = author
        instance.timestamp = time()
        return instance

    def __str__(self) -> str:
        """User-readable representation method"""
        return self.content

    def __repr__(self):
        """String object representation method"""
        return f'MyString(\'{self.content}\', \'{self.author}\')'


def main():
    new_string = MyString('test string', 'Me myself')
    print(new_string.upper())
    print(new_string.isdigit())
    print(f"{new_string.isalpha()=}")
    print(type(new_string.__str__()))
    print(new_string.isprintable())
    print(new_string.author)
    print(new_string.timestamp)
    print(new_string)


if __name__ == '__main__':
    main()
