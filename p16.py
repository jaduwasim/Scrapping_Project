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

df = pd.DataFrame(columns=titles)

row = table.find_all('tr')[1:]

for i in row:
	td = i.find_all('td')
	data = [tr.text.replace('\n','') for tr in td]
	l = len(df) #Initially length is 1 
	df.loc[l] = data #length increasing 1 by 1 and data will store one by one

df.to_csv('Stock_MarketData.csv')