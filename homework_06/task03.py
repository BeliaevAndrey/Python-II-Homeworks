from sem06_modules import ChessBoard
from itertools import permutations


def main():
    moves_pack = list()
    for line in permutations('abcdefgh'):
        moves_pack.append(tuple(''.join(pair) for pair in zip(line, '12345678')))
    print(len(moves_pack))
    for bunch in moves_pack:
        chess_board = ChessBoard()
        for qn, move in enumerate(bunch, start=1):
            chess_board.place(move, qn)
            print(chess_board)
        if chess_board.check_win():
            print(f'{" WIN!!! ":*^120}')
            print(chess_board)
            break
    else:
        print(f'{" FAIL!!! ":*^120}')

    # print(chess_board)
    # chess_board.place('b1', 1)
    # chess_board.place('c3', 2)
    # chess_board.place('e2', 3)
    # chess_board.place('h4', 4)
    # chess_board.place('f5', 5)
    # print(chess_board)
    # print(len(chess_board.get_beaten()), chess_board.get_beaten())


if __name__ == '__main__':
    main()
