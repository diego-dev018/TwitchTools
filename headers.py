from keys import SECRET_ID, CLIENT_ID
from os import path
import requests


def get_headers():
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': CLIENT_ID,
        'client_secret': SECRET_ID,
        'grant_type': 'client_credentials'
    }
    access_token = requests.post(url, params=params).json()['access_token']
    return {
        'Authorization': f'Bearer {access_token}',
        'Client-Id': CLIENT_ID
    }


if __name__ == '__main__':
    print(get_headers())