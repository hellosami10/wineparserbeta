#Author: Sami, Adnan


import sys

from bs4 import BeautifulSoup
import requests
from langdetect import detect
pg = str(sys.argv[1]);

source = requests.get('https://netra.news/2020/page/' + pg)
soup = BeautifulSoup(source.text, 'lxml')

content = soup.find_all('div', 'blog-desc text-center')
# content = content.find_all('h4')



for line in content:
	content = line.h4.a.text
	href = line.h4.a['href']
	

	if detect(content) == 'bn':
		print("<li><a target='_blank' href='"+ href +"'>" + content + "</a></li>")
	# with open('netra_dump.txt', "a", encoding="utf-8") as f:
	#     f.write(content)
	#     f.write('\n')

# print()
# print('Done !!')


