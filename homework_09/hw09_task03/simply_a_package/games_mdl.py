def guess(num_sc: int, attempts: int) -> str:
    """
    Guess game -- first you enter a secret number, then you guessing it back.
    This silly doc here is just for test.
    :param num_sc: int      -- cryptic number
    :param attempts: int    -- max amount of attempts
    :return: str            -- answer
    """
    result = 'Have not result yet'
    while attempts:
        print(f'left {attempts} attempts.', end=' ')
        attempts -= 1
        num = int(input('Input a number: '))
        if num == num_sc:
            print(f'Number found: {num}')
            break
        else:
            advice = ['lesser', 'greater']
            print(result := f'Your number is {advice[num > num_sc]} then right')
    else:
        print(result := f'You loose. Right number is {num_sc}')
    return result
