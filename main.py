from vod import save_vod
from keys import keys_main


def main():
    HEADERS = keys_main()
    options = [
        'GUARDAR VODS EN LOCAL',
        'EDITAR CLIPS'
    ]
    for n, option in enumerate(options):
        print(f'{n+1}) {option}')
    ans = input('> ')
    if ans == '1':
        pass
    elif ans == '2':
        pass
    else:
        pass


if __name__ == '__main__':
    main()