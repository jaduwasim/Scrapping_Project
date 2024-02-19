import requests
from bs4 import BeautifulSoup
import csv

with open('tablets.csv','w',newline='') as f:
	w = csv.writer(f)
	w.writerow(['Title','Price','Desc'])
	url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
	r = requests.get(url)

	soup = BeautifulSoup(r.text, 'html.parser')

	title = soup.find_all('a', class_= 'title')
	price = soup.find_all('h4', class_='float-end price card-title pull-right')
	desc = soup.find_all('p', class_ = 'description card-text')

	for t, p, d in zip(title, price, desc):
		w.writerow([t.string, p.string, d.string])
		print(f'{t.string}, {p.string}, {d.string}')
		print()
print('All Data Store in {f.name}')
f.close()