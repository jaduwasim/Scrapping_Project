# find Method

import requests
from bs4 import BeautifulSoup

url = 'https://www.rekhta.org/poets/bashir-badr/ghazals'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

# First Way
Fisrt_data = soup.find('h3', class_='noPoetSubTtl')
print(Fisrt_data.text)

# Second Way
Second_data = soup.find('h3', {'class':'noPoetSubTtl'})
print(Second_data.string)