#Author: Sami, Adnan

# import sys

from bs4 import BeautifulSoup
import requests

# date = str(sys.argv[1]);
# date = date.replace('/', '%2F')

source = requests.get("https://netra.news/2020/" )
soup = BeautifulSoup(source.text, 'lxml')

content = soup.find('div', class_='nav-links')
content = content.find_all('a')

last_index = len(content)
last_page_no = content[last_index-2].text
last_page_no = last_page_no.split(' ')
print(last_page_no[1])

# content = content.find_all('li')

# last_index = len(content) - 3 #GET LAST INDEX OF PAGI
# href = content[last_index].a['href']
# last_page_no = href.split('?')[1]
# last_page_no = href.split('=')[3]

# print(last_page_no)


