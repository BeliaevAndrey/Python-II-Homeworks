# Создайте класс с базовым исключением и дочерние классы-исключения:
# - ошибка уровня,
# - ошибка доступа.

class OwnBasicException(Exception):
    def __init__(self,  message: str):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class LevelError(OwnBasicException):
    def __init__(self, lvl_needed, lvl_given):
        super(LevelError, self).__init__(f'Wrong Level: {lvl_given=} lesser than {lvl_needed=}')


class AccessError(OwnBasicException):
    def __init__(self, u_id, u_name):
        super(AccessError, self).__init__(f'Access Denied User({u_id=}, {u_name=}) not in set of allowed.')


def main():
    # raise LevelError
    raise AccessError


if __name__ == '__main__':
    main()
