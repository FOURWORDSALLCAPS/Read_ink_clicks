import requests
from dotenv import load_dotenv
import os


def is_bitlink(authorization, user_input):
	url_bitlink = (
		f'https://api-ssl.bitly.com/v4/bitlinks/{user_input}'
	)
	response = requests.get(url_bitlink, headers=authorization)
	test = response.ok
	return test


def count_clicks(authorization, user_input):
	link = (
		f'https://api-ssl.bitly.com/v4/bitlinks/{user_input}/clicks/summary'
	)
	params = {
		'unit ': 'minute',
		'units ': '-1'
	}
	response = requests.get(link, headers=authorization, params=params)
	response.raise_for_status()
	test = response.json()
	return test['total_clicks']


def shorten_link(authorization, user_input):
	url = (
		'https://api-ssl.bitly.com/v4/shorten'
	)
	json = {
		'long_url': f'{user_input}'
	}
	response = requests.post(url, headers=authorization, json=json)
	response.raise_for_status()
	test = response.json()
	return test['id']

	
def main():
	user_input = (
		input('Введите ссылку: ')	
	)
	token_authorization = os.getenv('ACCESS_BITLY_TOKEN')	
	authorization = {
		'Authorization': f'Bearer {token_authorization}'
	}
	if not is_bitlink(authorization, user_input):
		try:
  			print ('Битлинк:', shorten_link(authorization, user_input))
		except requests.exceptions.HTTPError:
			print('Неправильная ссылка')
	else:
		try:
			print ('По вашей ссылке прошли:', count_clicks(authorization, user_input), 'раз(а)')
		except requests.exceptions.HTTPError:
			print('Неправильная ссылка')


if __name__ == '__main__':
	load_dotenv("dev.env")
	main()	







	
