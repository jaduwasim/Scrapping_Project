import pandas as pd 
import requests 
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

# Product Title
names = soup.find_all('a',class_='title')
product_name = []
for name in names:
	product_name.append(name.text)

#Product Prices
prices = soup.find_all('h4',class_='float-end price card-title pull-right')
price_list = []
for price in prices:
	price_list.append(price.text)


# Product Descriptions
Descriptions  = soup.find_all('p',class_='description card-text')
description_list = []
for desc in Descriptions:
	description_list.append(desc.text)


# Product Reviews
reviews = soup.find_all('p', class_='float-end review-count')
review_list = []
for review in reviews:
	review_list.append(review.text)




data_frame = pd.DataFrame({'Product Name': product_name, 'Product Price':price_list, 'Product Description':description_list, 'Product Review':review_list})
print(data_frame)
# data_frame.to_excel('Product_Details.csv')
data_frame.to_excel('Product_Details.xlsx') #for this you install openpyxl
print('All Data Store into Product_Details.csv')