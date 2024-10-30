from os import path, mkdir

DB_DIRNAME = 'DB'

if not path.exists(DB_DIRNAME):
    mkdir(DB_DIRNAME)

DB_FILES = {
    'keys': path.join(DB_DIRNAME, 'keys.pkl'),
    'vods': path.join(DB_DIRNAME, 'vods.pkl'),
}

DB_DIRS = {
    'vods': path.join(DB_DIRNAME, 'vods'),
    'vods_temp': path.join(DB_DIRNAME, 'vods_temp'),
    'clips_temp': path.join(DB_DIRNAME, 'clips_temp'),
    'clips': path.join(DB_DIRNAME, 'clips'),
}

def get_db_file(filename: str):
    if filename in DB_FILES:
        return DB_FILES[filename]
    

def get_db_dir(dirname: str):
    if dirname in DB_DIRS:
        if not path.exists(DB_DIRS[dirname]):
            mkdir(DB_DIRS[dirname])
        return DB_DIRS[dirname]
    

if __name__ == '__main__':
    print(get_db_dir('vods'))
