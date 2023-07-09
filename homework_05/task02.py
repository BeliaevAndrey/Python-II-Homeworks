# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import os


def function(some_path: str) -> tuple:
    if not os.path.isabs(some_path):
        some_path = os.path.abspath(some_path)
    return *some_path.rsplit('.', 1)[0].rsplit('/', 1), some_path.rsplit('.', 1)[1]


def main():
    path = ('/home/andrew/Documents/geekbrains/'
            'Python2023/Homeworks/homework_05/'
            'task02.test.file.with.bunch.of.dots.long_ext')
    path2 = ('task02.test.file.with.bunch.of.dots.long_ext')
    print(function(path))
    print(function(path2))


if __name__ == '__main__':
    main()
