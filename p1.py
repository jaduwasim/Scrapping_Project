# print Navigable

import requests
from bs4 import BeautifulSoup

url = 'https://www.rekhta.org/'
r = requests.get(url)

# soup = BeautifulSoup(r.text, 'html.parser')
soup = BeautifulSoup(r.content, 'html.parser')

nav = soup.header.div.p.string
title = soup.title
links = soup.find_all('a')
sources = soup.find_all('link')
print(f'Navigable: {nav}')
print(f'Website Title is : {title.string}')
print()
print('Links List:')
for link in links:
	href = link.get('href')
	if href:
		print(href)

for source in sources:
	hrefs = source.get('href')
	print(href)