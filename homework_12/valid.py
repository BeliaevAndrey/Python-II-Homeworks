SUBJECTS_FILE = 'subjects.csv'


class Marks:

    def __init__(self, lo_lim: int, hi_lim: int) -> None:
        self.lo_lim = lo_lim
        self.hi_lim = hi_lim

    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value):
        student = f'{instance.first_name} {instance.patronymic} {instance.last_name}'
        self.validate(value, student)
        setattr(instance, self.parameter_name, value)

    def validate(self, checked: dict, student_name):
        for i_subj, i_list in checked.items():
            self.validate_mark(i_list, i_subj, student_name)

    def validate_mark(self, mark_list: list, subj: str, student_name):
        for i_mark in set(mark_list):
            if not (self.lo_lim <= i_mark <= self.hi_lim):
                raise ValueError(f'{student_name}: Mark value: {i_mark} is out of range; subject: {subj}')


class Naming:

    def __init__(self, check_fst, response_fst, check_scd, response_scd):
        self.check_fst = check_fst
        self.check_scd = check_scd
        self.response_fst = response_fst
        self.response_scd = response_scd

    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value: str):
        if not self.check_fst(value):
            raise ValueError(self.response_fst + f': {value}')
        if not self.check_scd(value):
            raise ValueError(self.response_scd + f': {value}')
        setattr(instance, self.parameter_name, value)
