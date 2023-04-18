# Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.

from s13_t04_User_class import forming_fun, User
from s13_t03_Custom_Exceptions import AccessError, LevelError

ALLOWED_LEVEL = 5


class TaskFive:

    def __init__(self, file_name: str) -> None:
        self.users_set = forming_fun(file_name)
        self.authorized = set()

    @staticmethod
    def scan_uid_uname():
        while True:
            try:
                u_id = int(input('input user ID: '))
                break
            except ValueError as exc:
                print(f'{exc.__class__.__name__} {exc}      -- Integers only!')
        u_name = input('input user Name: ')
        return u_id, u_name

    def entrance(self, u_id: int = -1, u_name: str = ''):
        stub_level = 0
        if not u_name or u_id == -1:
            u_id, u_name = self.scan_uid_uname()
        tmp_user = User('0', str(u_id), u_name)
        if tmp_user not in self.users_set:
            raise AccessError(u_id=u_id, u_name=u_name)
        for i_user in self.users_set:
            if i_user == tmp_user and (stub_level := i_user.acs_level) >= ALLOWED_LEVEL:
                self.authorized.add(i_user)
                break
        else:
            raise LevelError(lvl_needed=ALLOWED_LEVEL, lvl_given=stub_level)

    def get_authorized(self):
        return self.authorized


def authorize(an_object: TaskFive, in_str: str):
    task_five = an_object
    try:
        eval(in_str)
    except (AccessError, LevelError) as exc:
        print(f'\033[31m{exc.__class__.__name__}: {exc}\033[0m')


def main():
    task_five = TaskFive('index.json')
    for item in ('task_five.entrance(2342, "asdfghj")',
                 'task_five.entrance(234324, "qwertyyuiop")',
                 'task_five.entrance(214235423, "zxcvbnm")',
                 'task_five.entrance(123, "name 5")',
                 'task_five.entrance(124, "name 3")',
                 'task_five.entrance(46, "sfsfsd")',
                 'task_five.entrance(46, "sfsfsd")',
                 'task_five.entrance(46, "sfsfsd")',
                 'task_five.entrance(46, "sfsfsd")',
                 'task_five.entrance(46, "sfsfsd")',
                 'task_five.entrance(46, "sfsfsd")',
                 'task_five.entrance(125, "name 2")',
                 'task_five.entrance(126, "name 1")',
                 'task_five.entrance(126, "name 1")',
                 'task_five.entrance(126, "name 1")',
                 'task_five.entrance(126, "name 2")',
                 'task_five.entrance(125, "name 1")',
                 'task_five.entrance(000, "Someone left")',
                 ):
        authorize(task_five, item)
    print(task_five.get_authorized())


if __name__ == '__main__':
    main()
