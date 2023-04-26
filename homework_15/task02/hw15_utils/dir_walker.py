# Каждый объект хранит:
#   - имя файла без расширения или название каталога,
#   - расширение, если это файл,
#   - флаг каталога,
#   - название родительского каталога.


import os
from collections import namedtuple
from common_log_util import common_log

FSObject = namedtuple('FSObject', 'name ext is_dir parent', defaults=['', '', False, ''])


def walk_dir(path_string: str):
    fs_objects = []
    if not path_string:
        path_string = os.getcwd()
        common_log.warning(f'Path setting default path (current dir): {path_string}')
    parent = path_string.rstrip('/').rsplit('/', 1)[1]
    try:
        for item in os.listdir(path_string):
            obj_name, obj_ext = None, None
            item = os.path.join(path_string, item)
            if os.path.isdir(item):
                item: str = item.rsplit('/', 1)[1]
                if item.rfind('.') != -1 and not item.startswith('.'):
                    obj_name, obj_ext = item.rsplit('.', 1)
                else:
                    obj_name = item
                fs_objects.append(FSObject(obj_name, obj_ext or '', True, parent))
            else:
                item: str = item.rsplit('/', 1)[1]
                if item.rfind('.') != -1 and not item.startswith('.'):
                    obj_name, obj_ext = item.rsplit('.', 1)
                else:
                    obj_name = item
                fs_objects.append(FSObject(name=obj_name, ext=obj_ext, parent=parent, is_dir=False))
            common_log.info(msg=str(fs_objects[-1]))
    except Exception as exc:
        print(f'\033[31mERROR: {exc.__class__.__name__}: {exc}\033[0m')
    return fs_objects


def main():
    for item in (walk_dir('')):
        print(repr(item))


if __name__ == '__main__':
    main()