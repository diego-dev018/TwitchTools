from manager_keys import get_keys_main
from os import path, remove
from pickle import load, dump
from sys import exit
import requests

FILENAME = path.join('db', 'header.pkl')


def get_headers_from_file():
    with open(FILENAME, 'rb') as f:
        return load(f)
    

def save_headers(headers):
    with open(FILENAME, 'wb') as f:
        dump(headers, f)


def get_headers():
    if path.exists(FILENAME):
        return get_headers_from_file()
    KEYS = get_keys_main()
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': KEYS['CLIENT_ID'],
        'client_secret': KEYS['SECRET_ID'],
        'grant_type': 'client_credentials'
    }
    try:
        access_token = requests.post(url, params=params).json()['access_token']
    except KeyError:
        print('Error: Invalid keys -> Check your keys :(')
        remove(path.join('db', 'keys.pkl'))
        exit(-1)
    header = {
        'Authorization': f'Bearer {access_token}',
        'Client-Id': KEYS['CLIENT_ID']
    }
    save_headers(header)
    return header


if __name__ == '__main__':
    print(get_headers())