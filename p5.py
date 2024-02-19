import requests
from bs4 import BeautifulSoup

url = 'https://www.rekhta.org/ghazals/aankhon-men-rahaa-dil-men-utar-kar-nahiin-dekhaa-bashir-badr-ghazals'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

data = soup.find('div', class_='c')
print(data.string)