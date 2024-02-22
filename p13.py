import requests
from bs4 import BeautifulSoup
url = 'https://www.rekhta.org/nazms/banjaara-naama-tuk-hirs-o-havaa-ko-chhod-miyaan-mat-des-bides-phire-maaraa-nazeer-akbarabadi-nazms'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
div = soup.find('div', class_='poemPageNote rpoemPageNote')
print(list(div)[3].text)

# Output :
'''

                    'Banjara-nama' is a famous Urdu poem by Nazeer Akhbarabadi, an Indian poet from the eighteenth century. It satirically conveys the message that worldly success is foolish and temporary, reminding us of the certainty of death for all.
Film: Sankalp (1974)
'''