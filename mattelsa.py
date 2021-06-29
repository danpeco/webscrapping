from bs4 import BeautifulSoup
import requests
import csv
import time

start_time = time.time()

# extracción de links para categorías hombre
base_url = 'https://www.mattelsa.net/hombre'
source = requests.get(base_url).text

soup = BeautifulSoup(source, 'lxml')
main = soup.find('main')
box_links = main.find('dl')

links = []

for i in box_links.find_all('a'):
    url = i.get('href')
    links.append(url)

print(links)
print('')

# Crear archivo csv y escribir titulos
with open ('mattelsa.csv', 'w') as mattelsa:

    f_writer = csv.writer(mattelsa)
    headers = ['tipo', 'descripción', 'precio']
    f_writer.writerow(headers)

    for i in links:

        sub_source = requests.get(i).text

        soup_s = BeautifulSoup(sub_source, 'lxml')
        main_s = soup_s.find('main')
        products = main_s.find(class_='products wrapper grid products-grid').ol

        for detail in products.find_all(class_='product details product-item-details'):

            type = detail.find('span', class_='first-product-name').text
            description = detail.find('span', class_='last-product-name').text
            price = detail.find('div').span.span.span.text.split()[0]

            print (type)
            print (description)
            print (price)
            print('')

            f_writer.writerow([type, description, price])

end_time = time.time()
running_time = end_time - start_time
print(f'The code took {running_time} seconds')


git_ejemplo_diff = 2 + 2
