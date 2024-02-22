# Scraping All List University 
import requests 
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Central_university_(India)'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
table = soup.find_all('table')[1]
headers = table.find('tr')
title = ['University','State','Location','Centralised','Established','Specialisation']
# for h in headers:
# 	if h.string :
# 		title.append(h.string.replace('\n',''))
# title.remove('Sources')
# print(title)
df = pd.DataFrame(columns=title)

row = table.find_all('tr')[1:]
for i in row:
	td = i.find_all('td')
	data = [r.text.replace('\n','') for r in td]
	data.remove(data[6])
	l = len(df)
	df.loc[l] = data

df.to_csv('University_list.csv')