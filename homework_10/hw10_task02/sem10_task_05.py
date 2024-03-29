# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Animal:
    def __init__(self, name: str, age: int, **_):
        self.name = name
        self.age = age

    def get_info(self) -> str:
        return (f'{"Type:":8}{type(self).__name__}'
                f'\n{"Name:":8}{self.name}'
                f'\n{"Age:":8}{self.age} years')


class Mammal(Animal):

    def __init__(self, name: str, age: int, hair: str, voice: str, **_):
        super().__init__(name, age)
        self.hair = hair
        self.voice = voice

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Hair:":8}{self.hair}'
                f'\n{"Voice:":8}{self.voice}'
                )


class Bird(Animal):

    def __init__(self, name: str, age: int, color: str, voice: str, **_):
        super().__init__(name, age)
        self.color = color
        self.voice = voice

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Color:":8}{self.color}'
                f'\n{"Voice:":8}{self.voice}'
                )


class Fish(Animal):

    def __init__(self, name: str, age: int, color: str, **_):
        super().__init__(name, age)
        self.color = color

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Color:":8}{self.color}'
                )


if __name__ == '__main__':
    print('Not for separate use')
