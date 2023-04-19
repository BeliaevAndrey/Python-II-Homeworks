import os

from homework_13.task_02.last_works import FileLister
from homework_13.task_02.custom_exceptions import (FileListerExtensionError,
                                                   FileListerObjectError,
                                                   FileListerPathError, )


class FileListerWorks:
    @classmethod
    def create_lister(cls, dir_path: str) -> FileLister:
        if os.path.exists(dir_path):
            return FileLister(dir_path)
        else:
            raise FileListerPathError

    @classmethod
    def list_dir(cls, lister: FileLister = None, file_ext: str = None, full_path: bool = True):
        if not lister:
            raise FileListerObjectError
        if not isinstance(lister, FileLister):
            raise FileListerObjectError
        if not file_ext:
            raise FileListerExtensionError
        return lister.list_files(file_ext, full_path)
