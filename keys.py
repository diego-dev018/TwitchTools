from os import path
import requests
import pickle as pkl


name_file = 'keys.pkl'


def save_keys():
    CLIENT_ID = input('CLIENT_ID (ID del CLIENTE) > ')
    SECRET_ID = input('SECRET_ID (CLAVE SECRETA) > ')
    with open(name_file, 'wb') as f:
        pkl.dump({'CLIENT_ID': CLIENT_ID, 'SECRET_ID': SECRET_ID}, f)
    return {'CLIENT_ID': CLIENT_ID, 'SECRET_ID': SECRET_ID}


def get_keys():
    with open(name_file, 'rb') as f:
        return pkl.load(f)
    
    
def get_accestoken(CLIENT_ID: str, SECRET_ID: str):
    url = 'https://id.twitch.tv/oauth2/token'
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': SECRET_ID,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, data=payload)
    # response.json()['acces_token']
    return get_headers(CLIENT_ID, response.json()['access_token'])


def get_headers(CLIENT_ID: str, AUTORIZATION: str):
    return {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {AUTORIZATION}'
    }


def keys_main():
    if not path.exists(name_file):
        keys = save_keys()
    else:
        keys = get_keys()
    headers = get_accestoken(keys['CLIENT_ID'], keys['SECRET_ID'])
    return headers
    


if __name__ == '__main__':
    print(keys_main())