# For get link from Multiple pages
import requests 
from bs4 import BeautifulSoup

for i in range(1,11):
	url = f'https://www.flipkart.com/mobiles-accessories/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D10000&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlVuZGVyICDigrkxMCwwMDAiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&wid=66.productCard.PMU_V2_18&page={i}'
	Base_Url = 'https://www.flipkart.com'
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'lxml')
	print(url)