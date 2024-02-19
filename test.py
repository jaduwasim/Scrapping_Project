import requests
from bs4 import BeautifulSoup
url = 'https://www.rekhta.org/poets/bashir-badr/ghazals?lang=hi'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

h3 = soup.find_all('h3', class_='noPoetSubTtl')
for i in h3:
	print(i.string)
