#extracting Ghazal from Rekhta by bashir badr
import requests
from bs4 import BeautifulSoup
import csv
url = 'https://www.rekhta.org/poets/bashir-badr/ghazals?lang=hi'
r = requests.get(url)
with open('bashi_hindi_ghazal.csv', 'w',newline='') as f:
	w = csv.writer(f)
	w.writerow(['Title'])
	soup = BeautifulSoup(r.text, "html.parser")

	h3 = soup.find_all('h3', class_='noPoetSubTtl')
	for i in h3:
		w.writerow([i.string])
print('All Data Store in bashi_hindi_ghazal.csv')