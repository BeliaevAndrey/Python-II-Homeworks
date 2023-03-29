import re
from hw03_fileworks import creator_m


class Display:
    _menu: tuple[str]
    _HR: str = '=' * 80
    _PROMPT: str = '_> '

    def __init__(self, menu: tuple[str]):
        self._menu = menu
        self.display_menu()

    def display_menu(self) -> None:
        self.display_text(self._HR)
        self.display_text(''.join([f'{point + 1:5}{sign}\n'
                                   for point, sign in enumerate(self._menu)]))
        self.obtain_pointer()

    @staticmethod
    def display_text(text):
        print(text)

    def obtain_pointer(self) -> str:
        while True:
            pointer = self.read_num('Enter point' + self._PROMPT)
            if 0 < pointer <= len(self._menu):
                return self._menu[pointer - 1]
            else:
                self.display_text("Wrong input. Try again")

    @staticmethod
    def read_num(prompt: str) -> [int, float]:
        num = input(prompt)
        if num.isdigit():
            return int(num)
        elif re.match(r"\d\.\d+", num):
            return float(num)
        else:
            return -1

    def read_string(self, prompt: str, limitations: tuple = None):
        result = input(prompt + self._PROMPT)
        while True:
            if limitations is None and result:
                return result
            elif result in limitations:
                result = input(prompt + self._PROMPT)
                return result
            else:
                self.display_text('Wrong input. Try again.')


class Controller:
    _ACTIONS: tuple[str] = ('CREATE FILES', 'GROUP RENAME', 'EXIT',)

    def __init__(self) -> None:
        self.display = Display(self._ACTIONS)

    def _collect_extensions(self) -> dict[str, int]:
        out_dict = {}
        while True:
            ext = self.display.read_string('Enter extension of files to create:')
            amt = self.display.read_num('Enter amount of files to create:')
            stopper = self.display.read_string('Finish? (y/n)', limitations=('y', 'Y', 'n', 'N'))
            out_dict[ext] = amt
            if stopper in ('y', 'Y'):
                return out_dict

    def mad_file_creator(self,) -> None:
        extensions_pack = self._collect_extensions()
        pack_string = f'{"extensions":^20}{"amount of files:":^20}'
        pack_string += '\n'.join([f'{ext:^20}{amt:^20}' for ext, amt in extensions_pack.items()]) + '\n'
        self.display.display_text(pack_string)
        stopper = self.display.read_string('Start? (y/n)', limitations=('y', 'Y', 'n', 'N'))
        if stopper in ('y', 'Y'):
            creator_m(extensions_pack)
        else:
            return

    def work(self):
        flag = True
        while flag:
            match self.display.obtain_pointer():
                case 'EXIT':
                    flag = False
                    print('Exiting... Bye!')

                case 'CREATE FILES':
                    ...
                case 'GROUP RENAME':
                    ...
                case _:
                    print("Internal Error")


def main():
    task03 = Controller()
    task03.work()


if __name__ == '__main__':
    main()
