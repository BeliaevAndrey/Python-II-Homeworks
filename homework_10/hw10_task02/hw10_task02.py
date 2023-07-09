# Доработаем задачи 5-6. Создайте класс-фабрику.
#   - Класс принимает тип животного (название одного из созданных классов)
#   и параметры для этого типа.
#   - Внутри класса создайте экземпляр на основе переданного типа и верните
#   его из класса-фабрики.
from sem10_task_05 import Mammal, Bird, Fish, Animal
from typing import Any


class AnimalFabric:

    def __new__(cls, animal_type, *args, **kwargs) -> [Mammal, Bird, Fish, Animal, Any]:
        try:
            tmp = super().__new__(animal_type)
            tmp.__init__(*args, **kwargs)
            return tmp
        except Exception as exc:
            print(f'{exc.__class__.__name__} {exc}')
            return Animal("Cadaver", 1000)


def main():
    dog = AnimalFabric(Mammal, name='Fido', age=5, voice='Woof!', hair='Pale, long')
    fish = AnimalFabric(Fish, name='Vanda', age=1, color='Rainbow')
    bird = AnimalFabric(Bird, name='Carl', age=8, color='Black', voice='CRAW!')
    unidentified = AnimalFabric('Non-type', name='Fail-Tester',
                                      age=100, color='Green', voice='Boo', hair='blonde')

    # dog = AnimalFabric.build(animal_type='Mammal', name='Fido', age=5, voice='Woof!', hair='Pale, long')
    # fish = AnimalFabric.build(animal_type='Fish', name='Vanda', age=1, color='Rainbow')
    # bird = AnimalFabric.build(animal_type='Bird', name='Carl', age=8, color='Black', voice='CRAW!')
    # unidentified = AnimalFabric.build(animal_type='Non-type', name='Fail-Tester',
    #                                   age=100, color='Green', voice='Boo', hair='blonde')
    print(dog.get_info(), '\n')
    print(fish.get_info(), '\n')
    print(bird.get_info(), '\n')
    print(unidentified.get_info())


if __name__ == '__main__':
    main()
