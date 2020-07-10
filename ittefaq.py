#Author: Sami, Adnan

import sys

from bs4 import BeautifulSoup
import requests

url = str(sys.argv[1])


source = requests.get(url)
soup = BeautifulSoup(source.text, 'lxml')

content = soup.find('div', id='main_content_list')
content = content.find_all('div', class_="allnews")




for line in content:
	href = line.find('a')['href']
	content = line.find('h5').text

	date = line.find('div', class_="post_date").text
	date = date.split(",");
	date = date[1].split(" ")
	date = date[1]

	if date == '১০':
		print("<li><a target='_blank' href='"+ href +"'>" + content + "</a></li>")
		css_class = "more"
	else:
		css_class = "end"
		break;
print("<button onclick='ittefaqGetPgNo()' class='"+ css_class +"'>"+"More</button>")

	