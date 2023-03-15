# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в
# качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

BACKPACK_LC = 15  # Load capacity, kg

JOURNEY_STUFF = {
    'walk': {
        'map': 0.2,
        'compass': 0.2,
        'bottle of water': 1.5,
    },
    'camp': {
        'axe': 2,
        'saw': 0.5,
        'tent': 2.4,
        'sleeping bag': 0.75,
        'matches': 0.01,
        'lantern': 0.3,
        'battery': 0.2,
        'radio': 0.4,
        'rope': 1.2,
        'book': 1.5,
    },
    'wardrobe': {
        'sweater': 0.8,
        'socks': 0.1,
        'pants': 0.7,
        'shirt': 0.5,
        't-shirt': 0.3,
        'gloves': 0.2,
    },
    'kitchen': {
        'pot': 1.2,
        'knife': 0.5,
        'spoon': 0.05,
        'cup': 0.15,
        'fork': 0.05,
    },
    'food': {
        'tinned meat': 1.4,
        'rice': 2,
        'salt': 0.2,
        'sugar': 0.4,
        'tea': 0.2,
        'coffee': 0.15,
    },
}


def prepare():
    whole_weight = sum((weight for thing in JOURNEY_STUFF.values() for weight in thing.values()))
    print(f'{" Whole weight: " + str(round(whole_weight, 3)) + " ":*^50}')
    totals = {item: weight for branch in JOURNEY_STUFF.values() for item, weight in branch.items()}
    return totals


def start_packing(totals: dict) -> tuple[dict, int, list]:
    total_weight = 0
    final_pack = {}
    dropped_things = []
    for i_thing in totals.items():
        total_weight += i_thing[1]
        final_pack.setdefault(*i_thing)
        while total_weight > BACKPACK_LC:
            dropped = final_pack.popitem()
            total_weight -= dropped[1]
            dropped_things.append(dropped)
    return final_pack, total_weight, dropped_things


def print_results(final_pack: dict, total_weight: int, dropped_things: list) -> None:
    print(f'{" Final weight: " + str(round(total_weight, 3)) + " ":*^50}')
    print(f'{" Final pack: ":*^50}')
    for i_thing, i_weight in sorted(final_pack.items()):
        print(i_thing, i_weight)
    print(f'{" Dropped: ":*^50}')
    for thing in dropped_things:
        print(*thing)


def main():
    print_results(*start_packing(prepare()))


if __name__ == '__main__':
    main()
