#Author: Sami, Adnan
#BD-PRATIDIN

from bs4 import BeautifulSoup
import requests

source = requests.get('https://barta24.com/')
soup = BeautifulSoup(source.text, 'lxml')

content = soup.find('div', id='latest')
content = content.find_all('div', class_="col-xs-12 p-t-10 p-b-10 br-bottom item")


for line in content:
	content = line.h3.text
	href = line.a['href']
	print("<li><a target='_blank' href='https://barta24.com/"+ href +"'>" + content + "</a></li>")
	print()

	# with open('barta24_dump.txt', "a", encoding="utf-8") as f:
	#     f.write(content)
	#     f.write('\n')

# print()
# print('Done !!')


