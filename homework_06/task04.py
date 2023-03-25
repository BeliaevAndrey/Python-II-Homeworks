from sem06_modules import task04_chess_module


def main():
    play = task04_chess_module.Searcher()
    play.start()
    print('Winning combinations:\n', '\n'.join(play.get_winning_strings()), '\n', sep='')
    print('\n'.join(f'Combination {i_key}:\n{i_board}'
                    for i_key, i_board in play.get_winning_boards().items()))


if __name__ == '__main__':
    main()
