import requests
from bs4 import BeautifulSoup

url = 'https://www.nike.com/in/w/mens-clothing-6ymx6znik1'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

div = soup.find('div', id='skip-to-products')
titles = div.find_all('div',class_='product-card__title')
for title in titles:
	print(title.string)
desc = div.find_all('div',class_='product-card__subtitle')
for i in desc:
	print(i.text)