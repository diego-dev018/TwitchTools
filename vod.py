from keys import keys_main
from datetime import datetime
from time import sleep
from os import mkdir, path
import requests
import subprocess

HEADERS = keys_main()


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

def get_dir(NAME_DIR: str):
    if not path.exists(NAME_DIR):
        mkdir(NAME_DIR)
    return NAME_DIR


DIR = get_dir('VODS')


def save_vod(vod_url: str):
    file_name = 'hola'
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
        print(f'VOD guardada con EXITO! en {file_name}')
    except subprocess.CalledProcessError as e:
        print(f'Error al guardar la VOD: {e.output}')


def get_vods(CHANNEL_ID: str):
    url = f'https://api.twitch.tv/helix/videos?user_id={CHANNEL_ID}'
    response = requests.get(url, headers=HEADERS).json()
    return response['data']


def get_channel_info(CHANNEL_NAME: str):
    url = f'https://api.twitch.tv/helix/users?login={CHANNEL_NAME}'
    response = requests.get(url, headers=HEADERS).json()
    return response['data'][0]['id']


def vod_main():
    CHANNEL_NAME = input('CHANNEL_NAME > ')
    CHANNEL_ID = get_channel_info(CHANNEL_NAME)
    vods = get_vods(CHANNEL_ID)
    for vod in vods:
        print(f'GUARDANDO > {vod['url']} | {vod['duration']} | {datetime.now()}')
        save_vod(vod['url'])
        sleep(5)
    return vods
    


if __name__ == '__main__':
    vod_main()