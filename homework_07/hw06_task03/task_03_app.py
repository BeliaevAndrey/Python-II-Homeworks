class Display:
    _MENU = ('CREATE FILES', 'GROUP RENAME')

    def __init__(self):
        self.display_text(self.display_menu())

    def display_menu(self) -> str:
        return '\n'.join([f'{point + 1:5}{sign}' for point, sign in enumerate(self._MENU)])

    @staticmethod
    def display_text(text):
        print(text)

    def obtain_pointer(self):
        ...

class Model:
    ...



def main():
    ...


if __name__ == '__main__':
    main()
