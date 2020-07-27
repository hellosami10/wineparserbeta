#Author: Sami, Adnan

import sys

from bs4 import BeautifulSoup
import requests

pg = str(sys.argv[1])


source = requests.get("https://www.ittefaq.com.bd/all-news/?pg=" + pg)
soup = BeautifulSoup(source.text, 'lxml')

content = soup.find('div', id='main_content_list')
content = content.find_all('div', class_="allnews")

current_date = soup.find('span', class_="date font-weight-bold").text
current_date = current_date.split(",")[1]
current_date = current_date.split(" ")[1]

flag = 1



for line in content:
	href = line.find('a')['href']
	content = line.find('h5').text

	date = line.find('div', class_="post_date").text
	date = date.split(",");
	date = date[1].split(" ")
	date = date[1]

	if date == current_date:
		print("<li><a target='_blank' href='"+ href +"'>" + content + "</a></li>")
		
	else:
		flag = 0
		break;

if flag == 1:
	print("<button onclick='ittefaqGetPgNo()' class='more'>"+"আরও দেখুন</button>")
else:
	print("<button onclick='' class='more-disabled'>"+"শেষ</button>")

	