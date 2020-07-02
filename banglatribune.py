#Author: Sami, Adnan
#Bangla Tribune

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.banglatribune.com/archive/')
soup = BeautifulSoup(source.text, 'lxml')


content = soup.find_all('div', class_='left_image_article')

for line in content:
	parent_tag = line.find('h2', class_='title_holder')

	content = parent_tag.span.text
	href = parent_tag.a['href']

	print("<li><a target='_blank' href='https://www.banglatribune.com"+ href +"'>" + content + "</a></li>")

#END