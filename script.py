import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import os

user_input = (
	input('Введите ссылку: ')	
)

json = {
	'long_url': f'{user_input}'
}
 
url = (
	'https://api-ssl.bitly.com/v4/shorten'
)

link = (
	f'https://api-ssl.bitly.com/v4/bitlinks/{user_input}/clicks/summary'
)
	
url_bitlink = (
	f'https://api-ssl.bitly.com/v4/bitlinks/{user_input}'
)

params = {
	'unit ': 'minute',
	'units ': '-1'
}

def is_bitlink(token, url_bitlink):
	response = requests.get(url_bitlink, headers=token)
	test = response.ok
	return test
	
def count_clicks(token, link):
	response = requests.get(link, headers=token, params=params)
	response.raise_for_status()
	test = response.json()
	return test['total_clicks']

def shorten_link(token, url, json):
	response = requests.post(url, headers=token, json=json)
	response.raise_for_status()
	test = response.json()
	return test['id']
	
def main():
	if is_bitlink(token, url_bitlink) == True:
		try:
  			print ('По вашей ссылке прошли:', count_clicks(token, link), 'раз(а)')
		except requests.exceptions.HTTPError:
			print('Неправильная ссылка')
	else:
		try:
			print ('Битлинк:', shorten_link(token, url, json))
		except requests.exceptions.HTTPError:
			print('Неправильная ссылка')
	 
if __name__ == '__main__':
	load_dotenv("dev.env")
	TOKEN = os.getenv('Access_Token')	
	token = {
		'Authorization': f'Bearer {TOKEN}'
	}
	main()	







	
