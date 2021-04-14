import os
import requests
import bs4

url = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
	print('\n[\033[0;36m*\033[0;0m] - Downloading page %s'%url)
	res = requests.get(url)
	try:
		res.raise_for_status()
	except Exception as exc:
		print('[\033[0;31m!\033[0;0m] - There was a problem: %s'%exc)
	soup = bs4.BeautifulSoup(res.text,'html.parser')
	elemComic = soup.select('#comic img');
	if elemComic == []:
		print('[\033[0;31m!\033[0;0m] Error 404 - Not Found')
	else:
		comicUrl = 'http:' + elemComic[0].get('src')
		print('[\033[0;36m*\033[0;0m] - Downloading image %s...'%(comicUrl))
		res_img = requests.get(comicUrl)
		try:
			res_img.raise_for_status()
		except Exception as exc:
			print('[\033[0;31m!\033[0;0m] - There was a problem: %s'%exc)
		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
		for chunck in res.iter_content(100000):
			imageFile.write(chunck)
		imageFile.close()
		prevLink = soup.select('a[rel="prev"]')[0]
		url = 'http://xkcd.com/' + prevLink.get('href')

print('\n[\033[0;32m+\033[0;0m] - Downloading Finished...')