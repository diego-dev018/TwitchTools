from os import path, mkdir
from files_name import DB

def make_db():
    if not path.exists(DB):
        mkdir(DB)

