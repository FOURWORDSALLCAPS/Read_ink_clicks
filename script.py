import requests
from dotenv import load_dotenv
from urllib.parse import urlparse
import os
import argparse


def is_bitlink(token, user_url):
    authorization = {'Authorization': f'Bearer {token}'}
    args_link = user_url.l
    http_test = urlparse(f'{args_link}')
    parse_1 = http_test.hostname
    parse_2 = http_test.path
    url_bitlink = f'https://api-ssl.bitly.com/v4/bitlinks/{parse_1}{parse_2}'
    response = requests.get(url_bitlink, headers=authorization)
    test = response.ok
    return test


def count_clicks(token, user_url):
    authorization = {'Authorization': f'Bearer {token}'}
    http_test = urlparse(f'{user_url}')
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


def shorten_link(token, user_url):
    authorization = {'Authorization': f'Bearer {token}'}
    url = 'https://api-ssl.bitly.com/v4/shorten'
    json = {'long_url': f'{user_url}'}
    response = requests.post(url, headers=authorization, json=json)
    response.raise_for_status()
    test = response.json()
    return test['link']


def main():
    parser = argparse.ArgumentParser(
        description='Программа может сжимать ссылки или выдавать количество переходов по ним'
    )
    parser.add_argument('l', help='Введите ссылку')
    user_url = parser.parse_args()
    token = os.getenv('ACCESS_BITLY_TOKEN')
    try:
        if not is_bitlink(token, user_url):
            print('Битлинк:', shorten_link(token, user_url.l))
        else:
            print('По вашей ссылке прошли:', count_clicks(token, user_url.l), 'раз(а)')
    except requests.exceptions.HTTPError:
        print('Неправильная ссылка')


if __name__ == '__main__':
    load_dotenv("dev.env")
    main()
