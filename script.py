import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import o

load_dotenv("dev.env")

TOKEN = os.getenv('TOKEN')

token = {
	'Authorization': f'Bearer {TOKEN}'
}

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

params = {
	'unit ': 'minute',
	'units ': '-1'
}
def is_bitlink(user_input):
	url_test = f'{user_input}'
	parsed = urlparse(url_test)
	if parsed.path[0:6] == 'bit.ly':
		def count_clicks(token, link):
			response = requests.get(link, headers=token, params=params)
			response.raise_for_status()
			return response.text[60]	

		try:
			if __name__ == '__main__':
  				print ('По вашей ссылке прошли:', count_clicks(token, link), 'раз(а)')
		except requests.exceptions.HTTPError:
			print('Неправильная ссылка')

	else:
		def shorten_link(token, url, json):
			response = requests.post(url, headers=token, json=json)
			response.raise_for_status()
			return response.text[47:61]

		try:
			if __name__ == '__main__':
				print ('Битлинк:', shorten_link(token, url, json))
		except requests.exceptions.HTTPError:
			print('Неправильная ссылка')
	
is_bitlink(user_input)



	
