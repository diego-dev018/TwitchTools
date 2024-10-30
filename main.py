from vod import vod_main
from keys import keys_main
from datetime import datetime
from extra_functions import get_db_dir


def main():
    get_db_dir()
    options = [
        'GUARDAR VODS EN LOCAL',
        'EDITAR CLIPS'
    ]
    for n, option in enumerate(options):
        print(f'{n+1}) {option}')
    ans = input('> ')
    if ans == '1':
        vod_main()
    elif ans == '2':
        pass
    else:
        pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\nSALIDA: {datetime.now()}')