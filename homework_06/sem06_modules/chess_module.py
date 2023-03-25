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

    def set_placement(self, placement: str) -> bool:
        """
        Obtain figures disposition
        :param placement: str -- string formatted as: "xN,xN,xN,xN,xN,xN,xN" x = a...h, N = 1...8
        :return: bool
        """
        placement.replace(' ', '')
        for qn, place in enumerate(placement.split(','), start=1):
            self.place_figure(coords=place, queen_num=qn)
        return self.check_win()

    def place_figure(self, coords: str, queen_num: int) -> None:
        """
        Places figure to the certain field of board
        :param coords: str -- coordinate string formatted as: "xN"
        :param queen_num: int -- number of queen
        :return: None
        """
        if len(coords) != 2:
            return
        col, row = list(coords)
        col, row = self._COLS.find(col), self._ROWS.find(row)
        if row == -1 or col == -1:
            return
        if (row, col) in self._beaten:
            return
        elif not self._check(row, col):
            return
        else:
            self._board[row][col] = queen_num
            self._check_moves(row, col)
            self._counter += 1

    def _check(self, row: int, col: int) -> bool:
        """Checks if a field is free"""
        if self._board[row][col] != 0:
            return False
        return True

    def _check_moves(self, row: int, col: int) -> None:
        """Updating set of fields beaten by a queen placed"""
        for j in range(self._SIDE):
            for i in range(self._SIDE):
                if (j == row and i == col
                        or j - i == row - col
                        or j + i == row + col
                        or j == row or i == col):
                    self._beaten.add((j, i))

    def __str__(self) -> str:
        out_str = '  '
        out_str += ''.join([f'{c: ^3}' for c in 'abcdefgh']) + '\n'
        out_str += f'\n'.join([f'{r_num:<2}' + ''.join([f'{i: ^3}' if i > 0
                                                        else f'{".":^3}' for i in row])
                               for r_num, row in enumerate(self._board, start=1)])
        return out_str + '\n'

    def get_beaten(self) -> set:
        """Get a bitten fields totals"""
        return self._beaten

    def check_win(self) -> bool:
        """Returns True if all 8 queens stand secure"""
        if self._counter == 8:
            return True
        return False


if __name__ == '__main__':
    chess_board = ChessBoard()
    print(chess_board.set_placement("a1,b7,c5,d8,e2,f4,g6,h3,"))
    print(chess_board.get_beaten())
    print(chess_board)

    chess_board = ChessBoard()
    print(chess_board.set_placement("d8,a1,c5,e2,f4,g6,h3,b7"))
    print(chess_board.get_beaten())
    print(chess_board)

    chess_board = ChessBoard()
    print(chess_board.set_placement("d8,a3,c5,e2,f4,g6,h3,b7"))
    print(chess_board.get_beaten())
    print(chess_board)

