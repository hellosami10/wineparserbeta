#Author: Sami, Adnan

from bs4 import BeautifulSoup
import requests

source = requests.get('https://bangla.bdnews24.com/archive/?date=2020-06-26')
soup = BeautifulSoup(source.text, 'lxml')

parent_tag = soup.find('ul', class_='contentUL')
child_tag = parent_tag.find_all('li')


for line in child_tag:
	content = line.span.a.text
	href = line.span.a['href']

	# #print("<li onclick='copy(this.innerHTML)'><a target="_blank" href='https://www.prothomalo.com"+ href +"'>" + content + "</a></li>")
	print("<li><a target='_blank' href='"+ href +"'>" + content + "</a></li>")
	# print()

	# content = parent_tag.h2.span

	# for link in href:
	# 	print("https://www.prothomalo.com" + link['href'])
	# 	print()

	# with open('bdnews_dump.txt', "a", encoding="utf-8") as f:
	#     f.write(content.strip())
	#     f.write('\n')

# print()
# print('Done !!')


