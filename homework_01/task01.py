# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на
# школьной тетрадке. (Взято из презентации семинара)

def multiplication_table() -> None:
    m_table = [[f'{i:<2}X{j:2} ={i * j:3}'
                for i in range(2, 10)]
               for j in range(2, 10)]

    for j in range(len(m_table)):
        for i in range(len(m_table[j])):
            print(m_table[j][i], end='\t')
        print()


def main():
    multiplication_table()


if __name__ == '__main__':
    main()
