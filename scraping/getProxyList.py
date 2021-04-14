import requests
import bs4

url = 'https://free-proxy-list.net/'

response = requests.get(url)
try:
	response.raise_for_status
except Exception as exc:
	print('[\033[0;31m!\033[0;0m] - There was a problem: %s'%(exc))
soup = bs4.BeautifulSoup(response.text,'lxml')
table = soup.find('table')
rows = table.find_all('tr')
for row in rows:
	proxies = row.contents[0].text+':'+row.contents[1].text+'\n'
	print(proxies)
	with open('proxies_list.txt','a') as file_object:
		file_object.write(proxies)

print("Finished")

