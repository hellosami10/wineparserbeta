#Author: Sami, Adnan

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.jagonews24.com/archive')
soup = BeautifulSoup(source.text, 'lxml')

content = soup.find_all('h3', class_='no-margin')

for line in content:
	content = line.a.text
	href = line.a['href']
	print("<li><a target='_blank' href='"+ href +"'>" + content + "</a></li>")
	print()

	# with open('jago_dump.txt', "a", encoding="utf-8") as f:
	#     f.write(content)
	#     f.write('\n')

# print()
# print('Done !!')


