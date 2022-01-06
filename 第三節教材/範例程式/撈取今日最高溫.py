from bs4 import BeautifulSoup
import requests

url = 'https://www.cwb.gov.tw/m/o/top10_temperature.htm'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

data = soup.select('#retab5 > div > div > table > tbody > tr:nth-child(1) > td.col1')

print(data[0].text)






