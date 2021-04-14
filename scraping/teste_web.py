import requests
import bs4

url = 'http://www.google.com/search'
item_search = 'hacking with python'
contador = 0
num = 5
parametros = {'q':item_search, 'start':contador, 'num':num}
headers = {
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/78.0.3904.108 Chrome/78.0.3904.108 Safari/537.36'
}
print('[\033[0;36m*\033[0;0m] - Googling...')
response = requests.get(url, params=parametros, timeout=60, headers=headers)
try:
	response.raise_for_status()
except Exception as exc:
	print('There was a problem: %s'%(exc))
soup = bs4.BeautifulSoup(response.text, 'lxml')
elems = soup.select('.r a')
for elem in elems:
	if elem.get('href') != '#' and not 'webcache' in elem.get('href'):
		try:
			print(elem.find('h3').get_text())
		except: 
			pass
		print(elem.get('href')+'\n')


