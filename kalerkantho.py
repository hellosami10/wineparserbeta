# from urllib.request import Request, urlopen   

# from bs4 import BeautifulSoup
# import requests

# #specify url
# url = 'https://www.kalerkantho.com/recent'
# req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
# response = urlopen(req, timeout=20).read()


# with open('ch.txt', "w", encoding="utf-8") as f:
#     f.write()



#Author: Sami, Adnan

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.kalerkantho.com/recent')
soup = BeautifulSoup(source.text, 'lxml')

parent_tag = soup.find('div', class_='col-xs-12 headline').h2.text

print(parent_tag)


# for line in child_tag:
# 	content = line.span.a.text
# 	href = line.span.a['href']

# 	# #print("<li onclick='copy(this.innerHTML)'><a target="_blank" href='https://www.prothomalo.com"+ href +"'>" + content + "</a></li>")
# 	print("<li><a target='_blank' href='"+ href +"'>" + content + "</a></li>")