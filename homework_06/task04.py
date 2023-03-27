from sem06_modules import task04_chess_module
from time import time_ns as _tns


def main():
    play = task04_chess_module.Searcher()
    start = _tns()
    play.brute_force()
    end1 = _tns() - start
    win_str = play.get_winning_strings()
    print('Using permutations')
    print('Number of wininning combinations:', len(win_str))
    print('Winning combinations:\n', '\n'.join(win_str), '\n', sep='')
    # print('\n'.join(f'Combination {i_key}:\n{i_board}'
    #                 for i_key, i_board in play.get_winning_boards().items()))

    print()
    play_random = task04_chess_module.RandomSearcher()
    start = _tns()
    play_random.start()
    end2 = _tns() - start
    print('Using random')
    win_str = play_random.get_winning_strings()
    print('Number of wininning combinations:', len(win_str))
    print('Winning combinations:\n', '\n'.join(win_str), '\n', sep='')
    # print('\n'.join(f'Combination {i_key}:\n{i_board}'
    #                 for i_key, i_board in play_random.get_winning_boards().items()))

    print(f'Time for permutations: {end1 / 1e9}; Time for random: {end2 / 1e9}; ')


if __name__ == '__main__':
    main()
