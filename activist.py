#Author: Sami, Adnan

import sys

from bs4 import BeautifulSoup
import requests

date = str(sys.argv[1]);
date = date.replace('/', '%2F')


source = requests.get('https://www.jagonews24.com/archive?dateFrom=' + date + '&dateTo=' + date + '&page=' + sys.argv[2])
soup = BeautifulSoup(source.text, 'lxml')

content = soup.find_all('h3', class_='no-margin')


for line in content:
	href = line.a['href']
	content = line.a.text

	print("<li><a target='_blank' href='"+ href +"'>" + content + "</a></li>")

# 	print(content)
# 	print()

	# with open('jjago_dump.txt', "a", encoding="utf-8") as f:
	#     f.write(content)
	#     f.write('\n')

# print()
# print('Done !!')


