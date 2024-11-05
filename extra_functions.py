from os import path, system
from pickle import dump, load
from sys import platform


def cleaner_screen():
    system('cls' if platform == 'win32' else 'clear')


def get_file(name_file: str):
    if not path.exists(name_file):
        return []
    with open(name_file, 'rb') as f:
        return load(f)
    

def intentar(argument):
    try:
        argument
    except Exception:
        pass


def save_file(name_file: str, data: list):
    if path.exists(name_file):
        data += get_file(name_file).copy()
    with open(name_file, 'wb') as f:
        dump(data, f)


if __name__ == '__main__':
    pass