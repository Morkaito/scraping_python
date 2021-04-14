import bs4
import sys
import re
import requests

def getProxiesList():
	proxies = []
	with open('proxies_list.txt','r') as file_object:
		for line in file_object:
			proxies.append(line.strip('\n'))

	return proxies

red = '\033[0;31m'
blue = '\033[0;36m'
green = '\033[0;32m'
white = '\033[0;0m'

contador = 0
consulta = ' '.join(sys.argv[1:])
num = 7
headers = {
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/78.0.3904.108 Chrome/78.0.3904.108 Safari/537.36'
}
parametros = {'q':consulta, 'start':contador, 'num':num}

def google_bot():
	print('\n['+blue+'*'+white+'] - Googling...\n')
	while True:
		response = requests.get('http://www.google.com.br/search', params=parametros, timeout=2, headers=headers)
		try:
			response.raise_for_status()
		except Exception as exc:
			print('\n['+red+'!'+white+'] - There was a problem: %s'%(exc))
		msg = 'Our systems have detected unusual traffic from your computer network'
		if msg in response.text:
			print('['+red+'!'+white+'] - Bot behavior has been detected. Exiting...')
			break
		soup = bs4.BeautifulSoup(response.text,'lxml')
		print('\n['+blue+'*'+white+'] - Extracting data...')
		divs = soup.find_all('div', {'class':'g'})
		for div in divs:
			try:
				print(div)
			except:
				pass

def google_bot_proxy():
	proxies = getProxiesList()
	proxy = proxies[0]
	proxies_failed = []
	proxies_detected_for_google = []
	fim = False
	print('\n['+blue+'*'+white+'] - Googling...\n')
	while True:
		try:
			print('['+blue+'*'+white+'] - Requesting server wait...')
			response = requests.get('http://www.google.com.br/search', params=parametros, timeout=10, headers=headers, proxies={'http':proxy})
		except Exception as exc:
			proxies_failed.append(proxy)
			try:
				proxy = proxies[proxies.index(proxy)+1]
				print('\n['+blue+'*'+white+'] - Changing proxy...')
			except IndexError:
				print('\n['+red+'!'+white+'] - Proxy limit exceded, this is not possible request\n['+green+'+'+white+'] - Finished')
				break
			else:
				continue
		msg = 'Our systems have detected unusual traffic from your computer network'
		if msg in response.text:
			a = re.search(r'(\d{1,3}\.){3}\d{1,3}', response.text)
			proxies_detected_for_google.append(a.group(0))
			try:
				proxy = proxies[proxies.index(proxy)+1]
			except IndexError:
				break
			else:
				continue
		print('['+green+'+'+white+'] - Extracting data...')
		soup = bs4.BeautifulSoup(response.text, 'lxml')
		print(soup)

if __name__ == '__main__':
	google_bot_proxy()