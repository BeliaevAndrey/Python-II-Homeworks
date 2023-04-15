class Marks:

    def __init__(self,
                 subjects: tuple[int],
                 lo_lim: int = 2,
                 hi_lim: int = 5,
                 amt_lim: int = 100, ) -> None:
        self.lo_lim = lo_lim
        self.hi_lim = hi_lim
        self.amt_lim = amt_lim
        self._subjects = dict.fromkeys(subjects, tuple())

    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.parameter_name, value)

    def validate(self, value):
        if not (self.lo_lim <= value <= self.hi_lim):
            raise ValueError(f'Mark value: {value} is out of range')


# class Marks:
#
#     def __init__(self,
#                  subjects: tuple[int],
#                  lo_lim: int = 2,
#                  hi_lim: int = 5,
#                  amt_lim: int = 100, ) -> None:
#         self.lo_lim = lo_lim
#         self.hi_lim = hi_lim
#         self.amt_lim = amt_lim
#         self._subjects = dict.fromkeys(subjects, tuple())
#
#     def __set_name__(self, owner, name):
#         self.parameter_name = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.parameter_name)
#
#     def __set__(self, instance, value):
#         self.validate(value)
#         setattr(instance, self.parameter_name, value)
#
#     def validate(self, value):
#         if not (self.lo_lim <= value <= self.hi_lim):
#             raise ValueError(f'Mark value: {value} is out of range')
#
#
class Naming:

    def __init__(self):
        self._name_set = False      # A kind of crutch

    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value):
        if not self._name_set:
            self.validate(value)
            setattr(instance, self.parameter_name, value)
            self._name_set = True
        else:
            raise AttributeError(f'Once set, parameter "{self.parameter_name}" cannot be changed')

    @staticmethod
    def validate(value: str):
        if not value.isalpha():
            raise ValueError("Only letters are allowed on names")
        if not value[0].isupper():
            raise ValueError("FIRST letter MUST be capital")
        for letter in value[1:]:
            if letter.isupper():
                raise ValueError("Only FIRST letter must be capital")

