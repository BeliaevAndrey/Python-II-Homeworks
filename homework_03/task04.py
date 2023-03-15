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


def start_packing(totals: dict) -> tuple[dict, int, dict]:
    total_weight = 0
    final_pack = {}
    dropped_things = {key: [] for key in JOURNEY_STUFF.keys()}
    for i_thing in totals.items():
        total_weight += i_thing[1]
        final_pack.setdefault(*i_thing)
        while total_weight > BACKPACK_LC:
            dropped = final_pack.popitem()
            total_weight -= dropped[1]
            dropped_things.setdefault(search(dropped[0]), [])
            dropped_things.get(search(dropped[0])).append(dropped)

    return final_pack, total_weight, dropped_things


def search(thing: str) -> str:
    for i_key, i_value in JOURNEY_STUFF.items():
        if thing in i_value.keys():
            return i_key


def form_table(final_pack: dict, total_weight: int, dropped_things: dict) -> str:

    def table_assembly(in_dict: dict, out_list: list = None) -> list:
        longest = len(max(table.values(), key=len))
        if out_list is None:
            out_list = []
        for i in range(longest):
            out_list.append(
                [f' {in_dict.get(key)[i][0]:15}{in_dict.get(key)[i][1]:5} | '
                 if i < len(in_dict.get(key)) else f' {"":20} | '
                 for key in in_dict.keys()
                 ])
        return out_list

    out_string = f'{" Backpack weight: " + str(round(total_weight, 3)) + " ":*^50}\n'
    table = {key: [] for key in JOURNEY_STUFF.keys()}
    for item in final_pack.items():
        category = search(item[0])
        table.setdefault(category, [])
        table[category].append(item)
    line = '|' + ''.join(f' {key:^20} | ' for key in table.keys()) + '\n|'

    out_string += line + '-'*(len(line) - 5) + '|\n|'
    rows = table_assembly(table)
    rows.append([f'{" Dropped things: ":-^{len(line) - 5}}|'])
    table_assembly(dropped_things, rows)

    out_string += '\n|'.join((''.join(row) for row in rows))
    return out_string


def main():
    print(form_table(*start_packing(prepare())))


if __name__ == '__main__':
    main()
