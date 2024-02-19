# print Navigable

import requests
from bs4 import BeautifulSoup

url = 'https://www.rekhta.org/'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

nav = soup.header.div.p.string
print(f'Navigable: {nav}')