import requests
import re
import bs4 
import sys
import webbrowser

if len(sys.argv) > 1:
	keyword_search = ''.join(sys.argv[2:])
	url = sys.argv[1]
	print('\n[\033[0;36m*\033[0;0m] - Googling...\n')
	res = requests.get(url)
	try:
		res.raise_for_status()
	except Exception as exc:
		print("[\033[0;31m!\033[0;0m] - There was a problem: %s"%(exc))
	soup = bs4.BeautifulSoup(res.text,'html.parser')
	linkElements = soup.select('.kCrYT a')
	numOpen = min(7, len(linkElements))
	regex = re.compile(r'youtube')
	for i in range(numOpen):
		mo = regex.search(linkElements[i].get('href'))
		if mo != None:
			pass
		else:
			webbrowser.open('https://www.google.com' + linkElements[i].get('href'))
else:
	print("Usage: python3 lucky.py <url> <keyword search>")