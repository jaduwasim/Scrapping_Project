import requests
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/clothing-and-accessories/bottomwear/pr?sid=clo,vua&p[]=facets.ideal_for%255B%255D%3DMen&p[]=facets.ideal_for%255B%255D%3Dmen&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_013a257c-ace2-48b5-8486-8b62b72641a2_1_372UD5BXDFYS_MC.8HARX8UX7IX5&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Fashion~Men%2527s%2BBottom%2BWear_8HARX8UX7IX5&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L1_view-all&cid=8HARX8UX7IX5'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

title = soup.find('div', class_='_2WkVRV')
print(title)