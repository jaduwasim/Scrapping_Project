# Scraping Data from https://iplt20.com/auction
import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = 'https://iplt20.com/auction'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
table = soup.find('table',id='t2')
title = ['PLAYER','NATIONALITY','TYPE','BASE PRICE']

# header = table.find('thead')
# scraped_title = []
# for i in header:
# 	if bool(i.text.replace('\n','')) == True:
# 		scraped_title.append(i.text.replace('\n',' '))
# title2 = []
# for i in scraped_title[0].split():
# 	print(i)

df = pd.DataFrame(columns=title)

table_row = table.find_all('tr')
for i in table_row[1:]:
	td = i.find_all('td')
	data = [tr.text for tr in td]
	l = len(df)
	df.loc[l]=data

print(df)
df.to_csv('IPL_Plyers_list.csv')
df.to_csv('IPL_Plyers_list.xlsx')
print('All Data Store in IPL_Plyers_list.csv')