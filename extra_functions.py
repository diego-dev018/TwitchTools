from os import path, mkdir, system
from json import load, dump
from platform import system as platform


def clear():
    system('cls' if platform() == 'Windows' else 'clear')


def make_db():
    if not path.exists('db'):
        mkdir('db')

def get_doc(filename: str):
    if not path.exists(filename):
        return None
    with open(filename, 'r') as file:
        return load(file)


def save_doc(filename: str, data: dict):
    if path.exists(filename):
        data = get_doc(filename) + data
    with open(filename, 'w') as file:
        dump(data, file, indent=4)


if __name__ == '__main__':
    # save_doc('test.json', [{'name': 'test3'}, {'name': 'test4'}])
    clear()