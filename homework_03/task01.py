""" (Задача не решенная на семинаре)
Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей. Ответьте на вопросы:
какие вещи взяли все три друга
какие вещи уникальны, есть только у одного друга
какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""
# FRIENDS = {   # simple test dictionary
#     'first': ('backpack', 'hooks', 'boat', 'knife',),
#     'second': ('backpack', 'hooks', 'knife', 'book',),
#     'third': ('backpack', 'hooks', 'knife', 'book',),
# }

FRIENDS = {
    'first': ('fishing rod', 'ball', 'book', 'backpack', 'hooks', 'knife', 'boat', 'knife', 'own unique FIRST THING'),
    'second': ('fishing rod', 'tent', 'sleeping bag', 'backpack', 'hooks', 'knife', 'own unique SECOND THING'),
    'third': ('matches', 'salt', 'pot', 'book', 'lantern', 'backpack', 'knife', 'own unique THIRD THING'),
}

all_things = set([item for items in FRIENDS.values() for item in items])

print(f'Total set of things for whole {len(FRIENDS)} persons:\n{"-" * 31}')
print('; '.join(all_things))

print(f'\nCommon things which has everyone:\n{"-" * 27}')
common_things = all_things.copy()
for friend in FRIENDS:
    common_things.intersection_update(set(FRIENDS[friend]))

print('; '.join([*sorted(common_things, key=len, reverse=True)]))

print(f'\nUnique things for everyone:\n{"-" * 27}')
for friend in FRIENDS:
    others = tuple(pers for pers in FRIENDS.keys() if pers != friend)
    things = set(item for item in (items for key in others for items in FRIENDS[key]))
    unique = set(FRIENDS[friend]).difference(things)
    if unique:
        print(f'{friend + ":":20}', end='')
        print('; '.join([*sorted(unique, key=len, reverse=True)]))

print(f'\nAbsent things for everyone:\n{"-" * 27}')
for friend in FRIENDS:
    print(f'{friend + " has not:":20}', end='')
    others = tuple(pers for pers in FRIENDS.keys() if pers != friend)
    things = set(item for item in (items for key in others for items in FRIENDS[key]))
    absent_things = things.difference(set(FRIENDS[friend]))
    if absent_things:
        print('; '.join([*(sorted(absent_things, key=len, reverse=True))]))
