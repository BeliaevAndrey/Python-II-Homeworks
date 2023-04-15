# Создайте класс студента.
#  - Используя дескрипторы проверяйте ФИО на первую заглавную букву и
#    наличие только букв.
#  - Названия предметов должны загружаться из файла CSV при создании
#    экземпляра. Другие предметы в экземпляре недопустимы.
#  - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
#    тестов (от 0 до 100).
#  - Также экземпляр должен сообщать средний балл по тестам для каждого
#    предмета и по оценкам всех предметов вместе взятых.
from a_student import Student

SUBJECTS_FILE = 'subjects.csv'


def main():
    user1 = Student('Vasily', 'Vasilievitch', 'Pupkin', SUBJECTS_FILE)
    print(user1)
    print(user1.subjects)
    try:
        user1.first_name = 'Veniamin'
    except Exception as exc:
        print(f'\033[31m{exc.__class__.__name__}: {exc}\033[0m')
    try:
        user1.subjects = ('A Housekeeping!',)
    except Exception as exc:
        print(f'\033[31m{exc.__class__.__name__}: {exc}\033[0m')
    print(user1)
    print(user1.marks)


if __name__ == '__main__':
    main()
