# Scraping a table from a website
import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://ticker.finology.in/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table',class_='table table-sm table-hover screenertable')
headers = table.find_all('th')
titles = []
for h in headers:
	titles.append(h.text)
print(titles)

df = pd.DataFrame(columns=titles)
print(df)