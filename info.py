from sys import exit
import requests


def get_channel_info(CHANNEL_NAME: str, HEADERS: dict, TYPE: str = 'id'):
    url = f'https://api.twitch.tv/helix/users?login={CHANNEL_NAME}'
    response = requests.get(url, headers=HEADERS).json()
    try:
        return response['data'][0][TYPE]
    except KeyError:
        print(f'ERROR: {response}')
        exit()


if __name__ == '__main__':
    from keys import keys_main
    print(get_channel_info('xqc', keys_main()))
