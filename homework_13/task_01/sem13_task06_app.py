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
    def read_uid_uname():
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
            u_id, u_name = self.read_uid_uname()
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


def main():
    task_five = TaskFive('index.json')
    for item in ((2342, "asdfghj"), (234324, "qwertyyuiop"), (214235423, "zxcvbnm"), (123, "name 5"),
                 (124, "name 3"), (46, "sfsfsd"), (46, "sfsfsd"), (46, "sfsfsd"), (46, "sfsfsd"),
                 (46, "sfsfsd"), (46, "sfsfsd"),(125, "name 2"), (126, "name 1"), (126, "name 1"),
                 (126, "name 1"), (126, "name 2"), (125, "name 1"), (000, "Someone left"),
                 ):
        try:
            task_five.entrance(*item)
        except (AccessError, LevelError) as exc:
            print(f'\033[31m{exc.__class__.__name__}: {exc}\033[0m')

    print(task_five.get_authorized())


if __name__ == '__main__':
    main()
