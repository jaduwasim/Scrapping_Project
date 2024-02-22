# Ectracting Data from Nested HTML tags or particular tags
import requests
from bs4 import BeautifulSoup
url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

# all_boxes = soup.find_all('div', class_='col-md-4 col-xl-4 col-lg-4')
box = soup.find_all('div', class_='col-md-4 col-xl-4 col-lg-4')[3]
# particular_p_tag = box.find_all('p')[2]
name = box.find('a')
print(name.string)
# desc = box.find('p')
desc = box.find('p', class_='description card-text')
print(desc.string)
# price = box.find('h4')
# price = box.find('h4',{'class':'float-end price card-title pull-right'})
price = box.find('h4',class_='float-end price card-title pull-right')
print(price.text)
# review = box.find_all('p')[1]
review = box.find('p',class_='float-end review-count')
print(review.string)