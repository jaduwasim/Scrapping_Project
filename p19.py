# Working Scraping from Multiple Pages
import requests
from bs4 import BeautifulSoup
import pandas as pd
titles = []
Prices = []
Descriptions = []
Reviews=[]

for i in range(1,3):
	url = 'https://www.flipkart.com/mobiles-accessories/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D10000&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlVuZGVyICDigrkxMCwwMDAiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&wid=66.productCard.PMU_V2_18&page='+str(i)
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'lxml')
	boxes = soup.find('div',class_='_1YokD2 _3Mn1Gg')
	names = boxes.find_all('div',class_='_4rR01T')
	for i in names:
		titles.append(i.text)

	prices = boxes.find_all('div',class_='_30jeq3 _1_WHN1')
	for p in prices:
		Prices.append(p.text)

	desc = soup.find_all('ul',class_='_1xgFaf')
	for i in desc:
		Descriptions.append(i.text)

	reviews = soup.find_all('div', class_='_3LWZlK')
	for r in reviews:
		Reviews.append(i.text)

print(len(titles))
print(len(Prices))
print(len(Descriptions))
print(len(Reviews))

df = pd.DataFrame({'Product':titles, 'Prices':Prices, 'Descriptions':Descriptions, 'Reviews':Reviews})
print(df)
# while True:
# 	next_page = soup.find('a',class_='_1LKTO3').get('href')
# 	cmplt_next_page = 'https://www.flipkart.com'+next_page
# 	print(cmplt_next_page)

# 	url = cmplt_next_page
# 	page = requests.get(url)
# 	soup2 = BeautifulSoup(page.text,'lxml')
# 	print(soup2)
