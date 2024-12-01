from extra_functions import make_db
from headers import get_headers
from sys import exit


def main():
    make_db()
    HEADER = get_headers()
    options = [
        'Vods automation',
    ]
    print('Welcome to the main menu')
    print('\'Ctrl\' + \'C\' to exit')
    print('Please select an option')
    for i, option in enumerate(options):
        print(f'{i + 1}) {option}')
    selected = input('> ')
    if selected == '1':
        pass
    else:
        print('Invalid option')
        input('Press enter to continue')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Exiting...')
        exit()