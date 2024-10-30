from os import path, mkdir
from pickle import dump, load

DB_DIRNAME = 'DB'
FILES_DIR = {
    'DB_VODS': path.join(DB_DIRNAME, 'vods.pkl'),
}

def get_file(name_file: str):
    with open(name_file, 'rb') as f:
        return load(f)


def save_file(name_file: str, data: list):
    if path.exists(name_file):
        data += get_file(name_file).copy()
    with open(name_file, 'wb') as f:
        dump(data, f)


def get_db_dir():
    if not path.exists(DB_DIRNAME):
        mkdir(DB_DIRNAME)


if __name__ == '__main__':
    get_db_dir()