import csv
from valid import Naming, Marks


class Student:
    first_name = Naming()
    patronymic = Naming()
    last_name = Naming()

    def __init__(self, first_name, patronymic, second_name, subjects_file):
        self.first_name = first_name
        self.patronymic = patronymic
        self.last_name = second_name
        with open(subjects_file, 'r', encoding='utf-8') as f_in:
            csv_reader = csv.reader(f_in, dialect='excel')
            self._subjects = tuple(next(csv_reader))
        self.marks = Marks(self._subjects)
        self.tests = Marks(self._subjects)

    def __str__(self):
        return f'{self.first_name} {self.patronymic} {self.last_name}'

    @property
    def subjects(self):
        return self._subjects

    @subjects.setter
    def subjects(self, value: tuple):
        if not self._subjects:
            self._subjects = value
        else:
            raise AttributeError(f'Once set, parameter "subjects" cannot be changed')


if __name__ == '__main__':
    print("Not for separate use")
