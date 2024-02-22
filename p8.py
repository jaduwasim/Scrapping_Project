import requests
from bs4 import BeautifulSoup

url = 'https://www.rekhta.org/poets/nazeer-akbarabadi/nazms'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
div = soup.find_all('div', class_='contentListItems nwPoetListBody')
for i in div:
	print(i.h3.string)
	print(i.h4.string)
	print()
