from pickle import load, dump
from os import path
from files_name import KEYS as FILENAME

# load -> Traer la informacion del fichero .pkl
# dumb -> Crea el fichero .pkl

def get_keys():
    with open(FILENAME, 'rb') as f:
        return load(f)
    

def make_keys():
    CLIENT_ID = input('CLIENT_ID >>> ')
    SECRET_ID = input('SECRET_ID >>> ')
    KEYS = {
        'CLIENT_ID': CLIENT_ID,
        'SECRET_ID': SECRET_ID
    }
    with open(FILENAME, 'wb') as f:
        dump(KEYS, f)
    return KEYS


def get_keys_main():
    if path.exists(FILENAME):
        keys = get_keys()
    else:
        keys = make_keys()
    return keys


if __name__ == '__main__':
    print(get_keys_main())
