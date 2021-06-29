#cambio para Git

import csv
from bs4 import BeautifulSoup
import requests

url = 'https://www.newegg.com/p/pl?d=GTX&N=-1&IsNodeId=1&bop=And&Page=1&PageSize=36&order=BESTMATCH'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

# with open (listado.csv, 'w') as listado:



f = open('listado.csv', 'w')

f_writer = csv.writer(f)
headers = ['brand', 'item', 'price']
f_writer.writerow(headers)

for container in soup.find_all('div', class_='item-container'):

        # brand = container.find('div', {'class': 'item-branding'}).a.img['alt']  #error when no brand on html
        item = container.find('a', {'class': 'item-title'}).text
        brand = item.split()[0]
        price = container.find('li', {'class': 'price-current'}).text.split()[0]

        print(brand)
        print(item)
        print(price)
        print('')


    f_writer.writerow([brand, item.replace(',', ''), price])

f.close()
