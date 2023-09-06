from valid import Naming, Marks

_LO_LIM_MARKS = 2
_HI_LIM_MARKS = 5
_LO_LIM_TESTS = 0
_HI_LIM_TESTS = 100


class Student:
    first_name = Naming(str.isalpha,
                        "Only letters are allowed in names",
                        str.istitle,
                        "First letter must be capital")
    patronymic = Naming(str.isalpha,
                        "Only letters are allowed in names",
                        str.istitle,
                        "First letter must be capital")
    last_name = Naming(str.isalpha,
                       "Only letters are allowed in names",
                       str.istitle,
                       "First letter must be capital")
    marks = Marks(_LO_LIM_MARKS, _HI_LIM_MARKS)
    tests = Marks(_LO_LIM_TESTS, _HI_LIM_TESTS)

    def __init__(self, first_name, patronymic, last_name):
        self.first_name = first_name
        self.patronymic = patronymic
        self.last_name = last_name

    def __str__(self):
        return (f'\n{"=" * 60}'
                f'\n{self.first_name} {self.patronymic} {self.last_name}'
                f'\nAverage mark on whole subjects: {self.get_marks_average()}'
                f'\nAverage tests balls for every subject:'
                f'\n{self.averages_str()}'
                f'\n{"=" * 60}')
 
    def get_tests_average(self) -> dict[str, float]:
        result = {}
        for i_subj, i_balls in self.tests.items():
            result[i_subj] = round(sum(i_balls) / len(i_balls), 3)
        return result

    def get_marks_average(self) -> float:
        result = []
        for i_marks in self.marks.values():
            result.append(sum(i_marks) / len(i_marks))
        return round(sum(result) / len(result), 3)

    def averages_str(self) -> str:
        return '\n'.join([f'{i_key + ":":_<30}{i_val:<10}'
                          for i_key, i_val in self.get_tests_average().items()])


if __name__ == '__main__':
    print("Not for separate use")
