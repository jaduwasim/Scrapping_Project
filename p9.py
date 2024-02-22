# Using Regular Expression

import re
import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
# soup = BeautifulSoup(page.text, 'lxml')
# soup = BeautifulSoup(string=re.comple('Lenovo'))
# soup = BeautifulSoup(string='Lenovo IdeaTab')
data = soup.find_all(string=re.compile('^L')) #Start from L
print(data)
