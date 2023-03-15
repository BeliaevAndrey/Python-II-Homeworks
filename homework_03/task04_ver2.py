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
    totals = {item: weight for branch in JOURNEY_STUFF.values() for item, weight in branch.items()}
    return totals


def repack(backpack_capacity: float = BACKPACK_LC) -> tuple[dict, int, float, dict]:   # totals: dict,
    total_weight = 0
    final_pack = {}
    dropped_things = {key: [] for key in JOURNEY_STUFF.keys()}
    count = 0
    while abs(total_weight - backpack_capacity) > 0.3:
        for category in JOURNEY_STUFF.keys():
            for thing in JOURNEY_STUFF[category].items():
                if thing[0] not in final_pack.keys():
                    count += 1
                    if total_weight + thing[1] < backpack_capacity:
                        total_weight += thing[1]
                        final_pack.setdefault(thing[0], thing[1])
                        break
                    else:
                        break

    for i_key, i_things in JOURNEY_STUFF.items():
        for j_key, j_weight in i_things.items():
            if j_key not in final_pack.keys():
                dropped_things[i_key].append((j_key, j_weight))

    return final_pack, total_weight, backpack_capacity, dropped_things


def search(thing: str) -> str:
    for i_key, i_value in JOURNEY_STUFF.items():
        if thing in i_value.keys():
            return i_key


def form_table(final_pack: dict,
               total_weight: int,
               backpack_capacity: float,
               dropped_things: dict) -> str:

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

    whole_weight = sum((weight for thing in JOURNEY_STUFF.values() for weight in thing.values()))
    whole_amount = sum(map(len, (things for things in JOURNEY_STUFF.values())))
    out_string = f'\n{" Whole weight of stuff: " + str(round(whole_weight, 3)) + " ":*^50}'
    out_string += f'\n{" Whole amount of stuff: " + str(whole_amount) + " ":*^50}'
    out_string += f'\n{" Backpack weight: " + str(round(total_weight, 3)) + " ":*^50}'
    out_string += f'\n{" Backpack load capacity: " + str(backpack_capacity) + " ":*^50}'
    table = {key: [] for key in JOURNEY_STUFF.keys()}
    for item in final_pack.items():
        category = search(item[0])
        table.setdefault(category, [])
        table[category].append(item)
    head_line = '\n|' + ''.join(f' {key:^20} | ' for key in table.keys()) + '\n|'
    out_string += head_line + '-' * (len(head_line) - 5) + '|\n|'
    rows = table_assembly(table)
    rows.append([f'{" Dropped things: ":-^{len(head_line) - 5}}|'])
    table_assembly(dropped_things, rows)

    out_string += '\n|'.join((''.join(row) for row in rows))
    return out_string


def main():
    with open('task04_result_ver2.txt', 'w', encoding='utf-8') as out_file:
        report = form_table(*repack())
        out_file.write(report)
        print(report)
        report = form_table(*repack(16))
        out_file.write(report)
        print(report)


if __name__ == '__main__':
    main()
