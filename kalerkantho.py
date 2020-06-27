from urllib.request import Request, urlopen    
from bs4 import BeautifulSoup
import requests

#specify url
url = 'https://www.kalerkantho.com/recent'
req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
response = urlopen(req, timeout=20).read()

soup = BeautifulSoup(response, 'lxml')

content = soup.find('div', class_='col-xs-12 headline').ul
content = content.find_all('li')

for line in content:
	content = line.a.text
	href = line.a['href']
	print("<li><a target='_blank' href='https://www.kalerkantho.com/"+ href +"'>" + content + "</a></li>")
	print()
