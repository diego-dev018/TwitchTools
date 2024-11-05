from keys import keys_main
from datetime import datetime
from time import sleep
from os import path
from sys import exit
from file_dirs import get_db_dir, get_db_file
from extra_functions import cleaner_screen, save_file, get_file
from time import sleep
from info import get_channel_info
import requests
import subprocess

""" def get_vod_info(VOD_ID: str):
    url = f'https://api.twitch.tv/helix/videos?id={VOD_ID}'
    response = requests.get(url, headers=HEADERS).json()['data'][0]
    return {
        'ID': response['id'],
        'user_name': response['user_name'],
        'title': response['title'],
        'created_at': response['created_at'],
        'url': response['url']
    } """


DIR = get_db_dir('vods')
DB_FILE_NAME = get_db_file('vods')

def save_vod(vod_url: str):
    file_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    save_name = path.join(DIR, f'{file_name}.mp4')
    command = [
        'streamlink',
        vod_url, 
        'best',
        '-o',
        save_name
    ]
    try:
        subprocess.run(command, check=True)
        print(f'VOD guardada con EXITO! en {save_name}')
    except subprocess.CalledProcessError as e:
        print(f'Error al guardar la VOD: {e.output}')


def get_vods(CHANNEL_ID: str):
    url = f'https://api.twitch.tv/helix/videos?user_id={CHANNEL_ID}'
    response = requests.get(url, headers=HEADERS).json()
    return response['data']


def vod_main():
    global HEADERS
    HEADERS = keys_main()
    CHANNEL_NAME = input('CHANNEL_NAME > ')
    CHANNEL_ID = get_channel_info(CHANNEL_NAME, HEADERS)
    while True:
        try:
            vods = get_vods(CHANNEL_ID)
            print(f'VODS DISPONIBLES: {len(vods)}')
            # sleep(60)
            for n, vod in enumerate(vods):
                if any([v['url'] == vod['url'] for v in get_file(DB_FILE_NAME)]):
                    print(f'VOD YA GUARDADA > {vod["title"]}')
                    sleep(30)
                    continue
                print(f'GUARDANDO > {vod['url']} | {vod['duration']} | {datetime.now().strftime("%H:%M:%S")} | {n+1}/{len(vods)}')
                save_vod(vod['url'])
                save_file(DB_FILE_NAME, [vod])
                sleep(30)
                cleaner_screen()
            sleep(6 * 60 * 60)
        except KeyboardInterrupt:
            print('SALIDA')
            break
    


if __name__ == '__main__':
    vod_main()