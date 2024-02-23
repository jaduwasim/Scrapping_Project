import requests 
from bs4 import BeautifulSoup

url = 'https://www.thecompanycheck.com/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
table = soup.find('table',class_='table tabl7h6g intested04')
first_row = table.find_all('span', class_='intest-title')
address = table.find_all('div',class_='money098')
for r,a in zip(first_row, address):
	print(f'Company:{r.text}, address:{a.text}')