from extra_functions import make_db, clear
from headers import get_headers
from sys import exit
from vods_automation import vods_automation as vods_auto


def main():
    make_db()
    options = [
        'Vods automation',
    ]
    print('Welcome to the main menu')
    print('\'Ctrl\' + \'C\' to exit')
    print('Please select an option')
    for i, option in enumerate(options):
        print(f'{i + 1}) {option}')
    selected = input('> ')
    clear()
    if selected == '1':
        vods_auto()
    else:
        print('Invalid option')
        input('Press enter to continue')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nExiting...')
        exit()
