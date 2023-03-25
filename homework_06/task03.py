from sem06_modules import ChessBoard
from itertools import permutations


def main():
    moves_pack = list()
    for line in permutations('abcdefgh'):
        moves_pack.append(tuple(''.join(pair) for pair in zip(line, '12345678')))
    for bunch in moves_pack:
        chess_board = ChessBoard()
        chess_board.set_placement(','.join(bunch))
        if chess_board.check_win():
            print(f'{" WIN!!! ":*^120}')
            print(chess_board)
            break
    else:
        print(f'{" FAIL!!! ":*^120}')


if __name__ == '__main__':
    main()
