from manager_keys import get_keys_main
import requests


def get_headers():
    KEYS = get_keys_main()
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': KEYS['CLIENT_ID'],
        'client_secret': KEYS['SECRET_ID'],
        'grant_type': 'client_credentials'
    }
    access_token = requests.post(url, params=params).json()['access_token']
    return {
        'Authorization': f'Bearer {access_token}',
        'Client-Id': KEYS['CLIENT_ID']
    }


if __name__ == '__main__':
    print(get_headers())