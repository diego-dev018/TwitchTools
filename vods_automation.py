from requests import get
from time import sleep
from os import path
from headers import get_headers as header
from api_global_functions import get_channel_id
from extra_functions import get_doc, save_doc

HEADER = header()


def download_vod(vod: dict):
    url = vod['url']
    response = get(url, headers=HEADER)
    if response.status_code == 200:
        data = response.json()
        for d in data['data']:
            download_url = d['url']
            response = get(download_url)
            if response.status_code == 200:
                with open(f'vods/{vod["title"]}.mp4', 'wb') as f:
                    f.write(response.content)
                sleep(1)
                return True
            else:
                print(f'Error downloading {vod["title"]}')
                return False
    else:
        print(f'Error downloading {vod["title"]}')
        return False


def download_vods(vods: list):
    for vod in vods:
        title = vod['title']
        print(f'Downloading {title}')
        download_status = download_vod(vod)
        if download_status == False:
            print(f'Error downloading {title}')
            continue
        save_doc(FILENAME, [vod])


def check_vods(vods: list):
    vods_checked = []
    if not path.exists(FILENAME):
        # print('¡NO VODS SAVED!')
        return vods
    data = get_doc(FILENAME)
    for vod in vods:
        for d in list(data):
            if vod['id'] == d['id']:
                break
        else:
            vods_checked.append(vod)
    return vods_checked


def get_vods(channel_id: int):
    url = f'https://api.twitch.tv/helix/videos?user_id={channel_id}'
    response = get(url, headers=HEADER)
    if response.status_code == 200:
        data = response.json()['data']
        return check_vods(data)
    return None


def main():
    global FILENAME
    hours_to_wait = 1
    channel = input('Enter the channel name: ')
    FILENAME = path.join('db', f'{channel}_vods_saved.json')
    channel_id = get_channel_id(channel)
    while True:
        vods = get_vods(channel_id)
        if len(vods) == 0:
            print('No vods to download!')
            return
        print('Vods to download:', len(vods))
        download_vods(vods)
        print(f'Waiting {hours_to_wait} hours to check for new vods...')
        sleep(hours_to_wait * 60 * 60)


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
