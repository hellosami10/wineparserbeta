#Author: Sami, Adnan
#PROTHOM-ALO

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.prothomalo.com/archive')
soup = BeautifulSoup(source.text, 'lxml')

parent_tag = soup.find_all('div', class_='each col_in image_no content_capability_blog content_type_article responsive_image_hide_ m_show_featured_image_as_left')


for line in parent_tag:
	content = line.h2.span.text
	href = line.a['href']
	#print("<li onclick='copy(this.innerHTML)'><a target="_blank" href='https://www.prothomalo.com"+ href +"'>" + content + "</a></li>")
	print("<li><a target='_blank' href='https://www.prothomalo.com"+ href +"'>" + content + "</a></li>")
	print()

	# content = parent_tag.h2.span

	# for link in href:
	# 	print("https://www.prothomalo.com" + link['href'])
	# 	print()

	# with open('pa_dump.txt', "a", encoding="utf-8") as f:
	#     f.write(con)
	#     f.write('\n')

# print()
# print('Done !!')


