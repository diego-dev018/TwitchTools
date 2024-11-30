from os import path, mkdir

def make_db():
    if not path.exists('db'):
        mkdir('db')

