# find_all() method
import csv
import requests
from bs4 import BeautifulSoup

with open('bashir.csv', 'w',newline='') as f:
	w = csv.writer(f)
	w.writerow(['Ghazal Title'])

	url = 'https://www.rekhta.org/poets/bashir-badr/ghazals'
	r = requests.get(url)

	soup = BeautifulSoup(r.text, 'html.parser')

	data_all = soup.find_all('h3', class_='noPoetSubTtl')
	for i in data_all:
		w.writerow([i.string])
		print(i.string)