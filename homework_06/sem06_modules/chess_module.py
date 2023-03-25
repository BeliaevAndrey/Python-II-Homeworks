__all__ = ['ChessBoard']


class ChessBoard:
    _SIDE: int = 8
    _board: list[list[int]] = None
    _COLS: str = 'abcdefgh'
    _ROWS: str = '12345678'
    _beaten: set = None
    _counter: int = None

    def __init__(self) -> None:
        self._board = [[0] * self._SIDE for _ in range(self._SIDE)]
        self._counter = 0
        self._beaten = set()
        print(f'INITED {self._beaten} {self._counter}')

    def place(self, coords: str, queen_num: int) -> None:
        if len(coords) != 2:
            # print('Wrong coordinates.')
            return
        col, row = list(coords)
        col, row = self._COLS.find(col), self._ROWS.find(row)
        if row == -1 or col == -1:
            # print(f'{queen_num}, Position out of board.')
            return
        if (row, col) in self._beaten:
            # print(f'{queen_num}, Position is beaten by another queen')
            return
        elif not self._check(row, col):
            # print(f'{queen_num}, Position occupied')
            return
        else:
            self._board[row][col] = queen_num
            # self._check_moves(row, col, queen_num)
            self._check_moves(row, col)
            self._counter += 1

    def _check(self, row: int, col: int) -> bool:
        if self._board[row][col] != 0:
            return False
        return True

    # def _check_moves(self, row: int, col: int, queen_num: int) -> None:
    def _check_moves(self, row: int, col: int) -> None:
        for j in range(self._SIDE):
            for i in range(self._SIDE):
                if (j == row and i == col
                        or j - i == row - col
                        or j + i == row + col
                        or j == row or i == col):
                    # self._board[j][i] = -queen_num
                    self._beaten.add((j, i))

    def __str__(self) -> str:
        out_str = '  '
        out_str += ''.join([f'{c: ^3}' for c in 'abcdefgh']) + '\n'
        out_str += f'\n'.join([f'{r_num:<2}' + ''.join([f'{i: ^3}' if i > 0
                                                        else f'{".":^3}' for i in row])
                               for r_num, row in enumerate(self._board, start=1)])
        return out_str + '\n'

    def get_beaten(self) -> set:
        return self._beaten

    def check_win(self) -> bool:
        if self._counter == 8:
            return True
        return False


if __name__ == '__main__':
    chess_board = ChessBoard()
    print(chess_board)
    chess_board.place('b1', 1)
    chess_board.place('c3', 2)
    chess_board.place('e2', 3)
    chess_board.place('h4', 4)
    chess_board.place('f5', 5)
    print(chess_board)
    print(len(chess_board.get_beaten()), chess_board.get_beaten())

