__all__ = ['guess_number_fun', 'get_results']

_results_dct = {}


def guess_number_fun(phrase: str, answers: list[str], attempts: int) -> int:
    print(phrase)
    start = attempts
    while attempts > 0:
        attempts -= 1
        guess = input('Enter your guess: ').lower()
        if guess in answers:
            report(phrase, start - attempts)
            return start - attempts
    report(phrase, 0)
    return 0


def report(phrase: str, att_amt: int) -> None:
    global _results_dct
    _results_dct[phrase] = att_amt


def get_results() -> str:
    global _results_dct
    return '\n'.join(
        (f'{i_key}\n{i_val}'
         for i_key, i_val in _results_dct.items()
         ))


if __name__ == '__main__':
    print("Not for separate use")
