from requests import get
from time import sleep
from os import path
from headers import get_headers as header
from api_global_functions import get_channel_id
from extra_functions import get_doc, save_doc

HEADER = header()
FILENAME = path.join('db', 'vods_saved.json')


def download_vods(vods: list):
    for vod in vods:
        save_doc(FILENAME, vod)
        input('Enter to continue...')


def check_vods(vods: list):
    vods_checked = []
    if not path.exists(FILENAME):
        print('¡NO VODS SAVED!')
        return vods
    data = get_doc(FILENAME)
    print(list(data))
    for vod in vods:
        if vod not in list(data):
            print(vod)
        input()


def get_vods(channel_id: int):
    url = f'https://api.twitch.tv/helix/videos?user_id={channel_id}'
    response = get(url, headers=HEADER)
    if response.status_code == 200:
        data = response.json()['data']
        return check_vods(data)
    return None


def main():
    channel = input('Enter the channel name: ')
    channel_id = get_channel_id(channel)
    vods = get_vods(channel_id)
    download_vods(vods)


def vods_automation():
    print('Welcome to the vods automation menu')
    print('\'Ctrl\' + \'C\' to exit')
    print('Please select an option')
    options = [
        'Only DOWNLOAD vods automatically',
        'Only UPLOAD to YouTube vods automatically',
        'DOWNLOAD and UPLOAD to YouTube vods automatically',
    ]
    for i, option in enumerate(options):
        print(f'{i + 1}) {option}')
    selected = input('> ')
    if selected == '1':
        main()
    elif selected == '2':
        main()
    elif selected == '3':
        main()
    else:
        print('Invalid option')
        input('Press enter to continue')


if __name__ == '__main__':
    main()
