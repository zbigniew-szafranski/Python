from os.path import exists
from typing import Tuple, Optional

def split_filename(filename: str)->Tuple[str, Optional[str]]:
    if '.' in filename:
        name, ext = filename.rsplit('.', maxsplit=1)
        return name, ext
    else:
        name, ext = filename, None
        return name, ext

def construct_filename(name: str, counter: int, ext: Optional[str])->str:
    if ext is None:
        ext_part = ''
    else:
        ext_part = '.' + ext
    return f'{name}_{counter}{ext_part}'

def generate_name(filename: str)->str:
    name, ext = split_filename(filename)

    if exists(filename):
        counter = 2
        while True:
            new_filename = construct_filename(name, counter, ext)
            if not exists(new_filename):
                break
            counter += 1
        return new_filename
    else:
        return filename