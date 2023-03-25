from sem06_modules import task04_chess_module
from time import time_ns as _tns


def main():
    play = task04_chess_module.Searcher()
    start = _tns()
    play.brute_force()
    end1 = _tns() - start
    print('Using permutations')
    print('Winning combinations:\n', '\n'.join(play.get_winning_strings()), '\n', sep='')
    print('\n'.join(f'Combination {i_key}:\n{i_board}'
                    for i_key, i_board in play.get_winning_boards().items()))

    print()
    play_random = task04_chess_module.RandomSearcher()
    start = _tns()
    play_random.start()
    end2 = _tns() - start
    print('Using random')
    print('Winning combinations:\n', '\n'.join(play.get_winning_strings()), '\n', sep='')
    print('\n'.join(f'Combination {i_key}:\n{i_board}'
                    for i_key, i_board in play.get_winning_boards().items()))

    print(f'Time for permutations: {end1 / 1e9}; Time for random: {end2 / 1e9}; ')


if __name__ == '__main__':
    main()
