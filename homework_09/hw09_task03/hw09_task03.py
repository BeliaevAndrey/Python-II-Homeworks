from simply_a_package import guess, para_checker_dec


@para_checker_dec
def starter(*args):
    guess(*args)


def main():
    starter(-1, -1)


if __name__ == '__main__':
    main()
