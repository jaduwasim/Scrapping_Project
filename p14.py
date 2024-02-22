# Scraping a table from a website

import requests
from bs4 import BeautifulSoup
url = 'https://ticker.finology.in/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table',class_='table table-sm table-hover screenertable')
tbody = table.find('tbody')
a = tbody.find_all('a')
for i in a:
	print(i.text)