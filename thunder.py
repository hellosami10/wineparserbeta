#Author: Sami, Adnan
#BD-PRATIDIN

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.bd-pratidin.com/')
soup = BeautifulSoup(source.text, 'lxml')

content = soup.find('div', class_='home-latest-news').ul
content = content.find_all('li')

for line in content:
	content = line.span.text
	href = line.a['href']
	print("<li><a target='_blank' href='https://www.bd-pratidin.com/"+ href +"'>" + content + "</a></li>")
	print()

	# with open('bdp_dump.txt', "a", encoding="utf-8") as f:
	#     f.write(content)
	#     f.write('\n')

# print()
# print('Done !!')


