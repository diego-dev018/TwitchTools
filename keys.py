from os import path, remove
from sys import exit
from extra_functions import get_file as get_keys, cleaner_screen
from file_dirs import get_db_file
import requests
import pickle as pkl


name_file = get_db_file('keys')


def save_keys():
    print(f'{'-' * 5} CLAVES NO ENCONTRADAS {'-' * 5}')
    CLIENT_ID = input('CLIENT_ID (ID del CLIENTE) > ')
    SECRET_ID = input('SECRET_ID (CLAVE SECRETA) > ')
    with open(name_file, 'wb') as f:
        pkl.dump({'CLIENT_ID': CLIENT_ID, 'SECRET_ID': SECRET_ID}, f)
    return {'CLIENT_ID': CLIENT_ID, 'SECRET_ID': SECRET_ID}
    
    
def get_accestoken(CLIENT_ID: str, SECRET_ID: str):
    url = 'https://id.twitch.tv/oauth2/token'
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': SECRET_ID,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, data=payload)
    # response.json()['acces_token']
    try:
        return response.json()['access_token']
    except KeyError:
        print('\nERROR EN LAS CLAVES. ESTAS SON INCORRECTAS O NO EXISTEN!')
        remove(name_file)
        return None


def get_headers(CLIENT_ID: str, CLIENT_SECRET: str):
    AUTORIZATION = get_accestoken(CLIENT_ID, CLIENT_SECRET)
    if AUTORIZATION:
        header = {
            'Client-ID': CLIENT_ID,
            'Authorization': f'Bearer {AUTORIZATION}'
        }
        if NEW_TYPE:
            header[NEW_TYPE[0]] = NEW_TYPE[1]
        return header
    return None


def keys_main(TYPE: list = None):
    global NEW_TYPE
    NEW_TYPE = TYPE
    HEADERS = None
    while not HEADERS:
        if not path.exists(name_file):
            keys = save_keys()
        else:
            keys = get_keys(name_file)
        HEADERS = get_headers(keys['CLIENT_ID'], keys['SECRET_ID'])
    return HEADERS
    


if __name__ == '__main__':
    if keys_main():
        print('Claves obtenidas con EXITO!')
        if input('Mostrar claves? (s/n) > ').lower() == 's':
            print(keys_main())
    else:
        print('Error al obtener las claves!')
    # {'Client-ID': 'rjonnkgfz...', 'Authorization': 'Bearer s6t53l5o...'}