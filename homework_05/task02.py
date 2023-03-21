# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def function(some_path: str) -> tuple[str, str, str]:
    path, name, ext = *some_path.rsplit('.', 1)[0].rsplit('/', 1), some_path.rsplit('.', 1)[1]
    return path, name, ext


def main():
    path = '/home/andrew/Documents/geekbrains/' + \
           'Python2023/Homeworks/homework_05/' + \
           'task02.test.file.with.bunch.of.dots.long_ext'
    print(function(path))


if __name__ == '__main__':
    main()
