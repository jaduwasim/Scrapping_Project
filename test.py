import requests
from bs4 import BeautifulSoup
import csv

Books_list = []
prices_list = []
availability_list = []
for i in range(1,51):
	url = f'https://books.toscrape.com/catalogue/page-{i}.html'
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'lxml')
	boxes = soup.find('ol',class_='row')
	Books = boxes.find_all('h3')
	Prices = boxes.find_all('p', class_='price_color')
	Avalibilty = boxes.find_all('i',class_='icon-ok')
	
	# for book, price, avb in zip(Books, Prices, Avalibilty):
	# 	if bool(book) == True:
	# 		Books_list.append(book.text.replace('\n',''))
	# 	prices_list.append(price.text.replace('\n',''))
	# 	availability_list.append(avb.text.replace('\n',''))
	for b, p, a in zip(Books, Prices, Avalibilty):
		if bool(b.text.replace('\n','')) == True:
			Books_list.append(b.text.replace('\n',''))
		# if bool(p.text.replace('\n','')) == True:
		prices_list.append(p.text.replace('\n',''))
		if bool(a.text.replace('\n','')) == True:
			Avalibilty.append(a.text.replace('\n',''))
print(len(Books_list))
print(len(Prices))
print(len(Avalibilty))