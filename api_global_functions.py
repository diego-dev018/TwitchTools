from requests import get
from headers import get_headers as header
from sys import exit

HEADER = header()


def get_channel_data(channel_name: str):
    url = f'https://api.twitch.tv/helix/users?login={channel_name}'
    data = get(url, headers=HEADER)
    return data.json()


def get_channel_id(channel_name: str):
    try:
        return get_channel_data(channel_name)['data'][0]['id']
    except IndexError:
        exit(f'¡{channel_name} NOT FOUND OR INVALID USERNAME!')


if __name__ == '__main__':
    print(get_channel_data('mixwell'))