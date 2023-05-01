import requests
from dotenv import load_dotenv
from urllib.parse import urlparse
import os


def is_bitlink(authorization, user_input):
    http_test = urlparse(f'{user_input}')
    parse_1 = http_test.hostname
    parse_2 = http_test.path
    url_bitlink = f'https://api-ssl.bitly.com/v4/bitlinks/{parse_1}{parse_2}'
    response = requests.get(url_bitlink, headers=authorization)
    test = response.ok
    return test


def count_clicks(authorization, user_input):
    http_test = urlparse(f'{user_input}')
    parse_1 = http_test.hostname
    parse_2 = http_test.path
    link = f'https://api-ssl.bitly.com/v4/bitlinks/{parse_1}{parse_2}/clicks/summary'
    params = {
        'unit ': 'minute',
        'units ': '-1'
    }
    response = requests.get(link, headers=authorization, params=params)
    response.raise_for_status()
    test = response.json()
    return test['total_clicks']


def shorten_link(authorization, user_input):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    json = {'long_url': f'{user_input}'}
    response = requests.post(url, headers=authorization, json=json)
    response.raise_for_status()
    test = response.json()
    return test['link']


def main():
    user_input = input('Введите ссылку: ')
    token_authorization = os.getenv('ACCESS_BITLY_TOKEN')
    authorization = {'Authorization': f'Bearer {token_authorization}'}
    try:
        if not is_bitlink(authorization, user_input):
            print('Битлинк:', shorten_link(authorization, user_input))
        else:
            print('По вашей ссылке прошли:', count_clicks(authorization, user_input), 'раз(а)')
    except requests.exceptions.HTTPError:
        print('Неправильная ссылка')


if __name__ == '__main__':
    load_dotenv("dev.env")
    main()
