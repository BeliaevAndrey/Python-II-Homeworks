import re
import os
from hw03_fileworks import creator_m, grp_rename


class Display:
    _menu: tuple[str]
    _HR: str = '=' * 80
    _PROMPT: str = '_> '

    def __init__(self, menu: tuple[str]) -> None:
        self._menu = menu

    def display_menu(self) -> None:
        self.display_text(self._HR)
        self.display_text(''.join([f'{point + 1:<5}{sign}\n'
                                   for point, sign in enumerate(self._menu)]))

    @staticmethod
    def display_text(text) -> None:
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

    def read_string(self, prompt: str,
                    limitations: tuple = None,
                    empty_allowed: bool = False) -> str:
        while True:
            result = input(prompt + self._PROMPT)
            if limitations is None and result:
                return result
            elif limitations and result in limitations:
                return result
            else:
                if not result and empty_allowed:
                    return ''
                self.display_text('Wrong input. Try again.')


class Controller:
    _ACTIONS: tuple[str] = ('CHOOSE WORKING DIRECTORY', 'CREATE FILES', 'GROUP RENAME', 'EXIT',)
    _working_directory: str = None
    _SPECIALS = r"~`!@#$%^&*()\"<>' "

    def __init__(self) -> None:
        self.display = Display(self._ACTIONS)
        self._working_directory = os.getcwd()
        self._print_work_dir()

    def _collect_extensions(self) -> dict[str, int]:
        out_dict = {}
        while True:
            ext = self.display.read_string('Enter extension of files to create:')
            amt = self.display.read_num('Enter amount of files to create:')
            stopper = self.display.read_string('Finish? (y/n)', limitations=('y', 'Y', 'n', 'N'))
            out_dict[ext] = amt
            if stopper in ('y', 'Y'):
                return out_dict

    def _print_work_dir(self) -> None:
        self.display.display_text('CURRENT WORKING DIRECTORY:')
        self.display.display_text(self._working_directory)

    def mad_file_creator(self) -> None:
        extensions_pack = self._collect_extensions()
        pack_string = f'{"extensions":^20}{"amount of files:":^20}\n{"-" * 40:^40}\n'
        pack_string += '\n'.join([f'{ext:^20}{amt:^20}' for ext, amt in extensions_pack.items()]) + '\n'
        self.display.display_text(pack_string)
        stopper = self.display.read_string('Start? (y/n)', limitations=('y', 'Y', 'n', 'N'))
        if stopper in ('y', 'Y'):
            creator_m(extensions_pack)
        else:
            return

    def _validate_path(self, path: str) -> bool:
        if path == '':
            return False
        for smb in path:
            if smb in self._SPECIALS:
                return False
        return True

    def change_work_dir(self):
        self._print_work_dir()
        new_path = ''
        while not self._validate_path(new_path):
            new_path = self.display.read_string('Enter new ABSOLUTE path')
            if '\\' in new_path:
                new_path = os.path.join(*new_path.split('\\'))

        if os.path.isdir(new_path):
            self.display.display_text("Changing to new directory")
            self._working_directory = new_path
        else:
            self.display.display_text("Creating new directory")
            os.makedirs(new_path)
            self._working_directory = new_path
        os.chdir(self._working_directory)
        self._print_work_dir()

    def _collect_data_on_renaming(self) -> dict[str, [str, int]]:
        out_dict = {'src_extension': self.display.read_string('Enter extension of files to rename')}
        while True:
            lower_lim = self.display.read_num(
                'Enter lower limit of source filename symbols to be added to new name _> ')
            upper_lim = self.display.read_num(
                'Enter upper limit of source filename symbols to be added to new name _> ')
            counter_length = self.display.read_num(
                'Enter amount of digits in counter to be added to new name _> ')
            if 0 <= upper_lim < 256 and 0 <= lower_lim < 256 and 0 < counter_length < 10:
                out_dict['origin_range'] = (lower_lim, upper_lim)
                out_dict['number_digits_amt'] = counter_length
                break
            else:
                self.display.display_text('Wrong input. Try again.')
        out_dict['dst_extension'] = self.display.read_string(
            'Enter new extension of file (if needed)',
            empty_allowed=True)
        out_dict['dst_file_name'] = self.display.read_string('Enter new filename (if needed)', empty_allowed=True)
        return out_dict

    def start_group_rename(self) -> None:
        files_to_rename_dct = self._collect_data_on_renaming()
        info_string = '\n'.join([f'{i_key:20}{i_val}' for i_key, i_val in files_to_rename_dct.items()])
        self.display.display_text('Rename parameters:' + '\n')
        self.display.display_text(info_string + '\n')
        stopper = self.display.read_string('Start? (y/n)', limitations=('y', 'Y', 'n', 'N'))
        if stopper in ('y', 'Y'):
            report = grp_rename(**files_to_rename_dct)
            self.display.display_text("Files processed:")
            self.display.display_text(''.join([f'File: {item[0]} moved to: {item[1]}\n' for item in report]))
        else:
            return

    def work(self) -> None:
        flag = True
        while flag:
            self.display.display_menu()
            choice = self.display.obtain_pointer()
            self.display.display_text(f'YOUR CHOICE: {choice}')
            match choice:
                case 'EXIT':
                    flag = False
                    print('Exiting... Bye!')
                case 'CREATE FILES':
                    self.mad_file_creator()
                case 'GROUP RENAME':
                    self.start_group_rename()
                case 'CHOOSE WORKING DIRECTORY':
                    self.change_work_dir()
                case _:
                    print("Internal Error")


def main():
    task03 = Controller()
    task03.work()


if __name__ == '__main__':
    main()
