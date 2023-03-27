"""Modification of chess module for task 3 """
__all__ = ['ChessBoard', 'Searcher', 'RandomSearcher']

from itertools import permutations
from random import shuffle as _sfl
from math import factorial as _fct


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


class Searcher:
    """Searching wining combinations of queen placement"""
    _winning_strings: set[str] = None
    _win_boards: dict[str, ChessBoard] = None
    _current_board: ChessBoard = None

    def __init__(self):
        self._winning_strings = set()
        self._win_boards = {}
        self.new_board()

    def new_board(self) -> None:
        self._current_board = ChessBoard()

    def brute_force(self):
        """Search of winning combination based on permutations function from itertools module"""
        moves_pack = list()
        for line in permutations('abcdefgh'):
            moves_pack.append(tuple(''.join(pair) for pair in zip(line, '12345678')))
        count = 0
        for bunch in moves_pack:
            self.new_board()
            count += 1
            self._current_board.set_placement(','.join(bunch))
            if self._current_board.check_win():
                self._winning_strings.add(','.join(sorted(bunch)))
                self._win_boards[','.join(sorted(bunch))] = self._current_board
                self.new_board()
                if len(self._winning_strings) > 100:
                    break

    def get_winning_strings(self) -> set[str]:
        return self._winning_strings

    def get_winning_boards(self) -> dict[str, ChessBoard]:
        return self._win_boards


class RandomSearcher:
    """Searching wining combinations of queen placement"""
    _winning_strings: set[str] = None
    _win_boards: dict[str, ChessBoard] = None
    _current_board: ChessBoard = None
    _used_combs = set()
    _LETTERS = list('abcdefgh')
    _STOP_NUM = _fct(len(_LETTERS))

    def __init__(self):
        self._winning_strings = set()
        self._win_boards = {}
        self._new_board()

    def _new_board(self) -> None:
        self._current_board = ChessBoard()

    def start(self):
        """Search of winning combination based on random combinations of moves"""
        count = 0
        while len(self._winning_strings) < 92 and count < self._STOP_NUM * 10:
            count += 1
            self._new_board()
            letters = list('abcdefgh')
            _sfl(letters)
            string = ','.join(f'{i+1}{letters[i]}' for i in range(8))
            while string not in self._used_combs:
                letters = list('abcdefgh')
                _sfl(letters)
                string = ','.join(sorted([f'{letters[i]}{i+1}' for i in range(8)]))
                self._used_combs.add(string)
            self._current_board.set_placement(string)
            if self._current_board.check_win():
                self._winning_strings.add(string)
                self._win_boards[string] = self._current_board
        # print('COUNT: ', count)

    def get_winning_strings(self) -> set[str]:
        return self._winning_strings

    def get_winning_boards(self) -> dict[str, ChessBoard]:
        return self._win_boards

    def get_used(self) -> set[str]:
        return self._used_combs


if __name__ == '__main__':
    print("Used in task 4 only")
