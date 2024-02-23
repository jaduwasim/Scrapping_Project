# Ecxtractic Data from The Company Check...
import requests
from bs4 import BeautifulSoup
import csv
with open('company_check.csv', 'w', newline='') as f:
	w = csv.writer(f)
	w.writerow(['Company Name', 'Address','Status'])

	for i in range(1,51):
		url = 'https://www.thecompanycheck.com/company-directory/'+str(i)
		page = requests.get(url)
		soup = BeautifulSoup(page.text,'lxml')
		boxes = soup.find('div',class_='col-md-8 part2 tabdirct092')
		company_name = boxes.find_all('button',class_='cursor border-effect')
		company_address = boxes.find_all('p', class_='mb-1 directoryc1')
		status = boxes.find_all('p',class_='active_greentext mb-2')
		for comp, add, st in zip(company_name, company_address, status):
			w.writerow([comp.text, add.text, st.text])

print('All Data Store in companay_check.csv')

			