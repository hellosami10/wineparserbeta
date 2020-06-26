#Author: Sami, Adnan

import sys

from bs4 import BeautifulSoup
import requests

date = str(sys.argv[1]);
date = date.replace('/', '%2F')


source = requests.get('https://www.jagonews24.com/archive?dateFrom=' + date + '&dateTo=' + date)
soup = BeautifulSoup(source.text, 'lxml')

content = soup.find('ul', class_='pagination')
content = content.find_all('li')

last_index = len(content) - 3 #GET LAST INDEX OF PAGI
href = content[last_index].a['href']
last_page_no = href.split('?')[1]
last_page_no = href.split('=')[3]

print(last_page_no)





# for line in content:
# 	content = line.a
# 	# href = line.a['href']
# 	# print("<li><a target='_blank' href='https://www.bd-pratidin.com/"+ href +"'>" + content + "</a></li>")
# 	print(content)
# 	print()

# with open('bdp_dump.txt', "a", encoding="utf-8") as f:
#     f.write(content)
#     f.write('\n')

# print()
# print('Done !!')


