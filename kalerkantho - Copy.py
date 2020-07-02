from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.kalerkantho.com/recent')
soup = BeautifulSoup(source.text, 'lxml')

content = soup.find('div', class_='col-xs-12 headline').ul
content = content.find_all('li')

for line in content:
	content = line.a.text
	href = line.a['href']
	print("<li><a target='_blank' href='https://www.kalerkantho.com/"+ href +"'>" + content + "</a></li>")
	print()
