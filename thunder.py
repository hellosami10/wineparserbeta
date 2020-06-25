#Author: Sami, Adnan
#BD-PRATIDIN

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.bd-pratidin.com/')
soup = BeautifulSoup(source.text, 'lxml')

content = soup.find('div', class_='home-latest-news').ul
content = content.find_all('span')

for line in content:
	con = line.text
	print("<li onclick='copy(this.innerHTML)'>" + con + "</li>")
	print()

# 	# with open('bdp_dump.txt', "a", encoding="utf-8") as f:
# 	#     f.write(con)
# 	#     f.write('\n')

# print()
# print('Done !!')


