import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

url = 'https://www.newegg.com/tools/custom-pc-builder/pl/ID-147/Page-{page}?diywishlist=0'
file = open('desktop_memory.csv', mode='w', newline='\n')
csv_obj = csv.writer(file)
csv_obj.writerow(['Model', 'Price'])

for page in range(1, 6):
    url1 = url.format(page=page)
    r = requests.get(url1)
    print(r)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    desktop_memory_soup = soup.find('table', class_='table-vertical')
    all_desktop_memory = desktop_memory_soup.find_all('td', class_='td-item')
    all_desktop_memory_price = desktop_memory_soup.find_all('li', class_='price-current')


    for desktop_memory, desktop_memory_price in zip(all_desktop_memory, all_desktop_memory_price):
        model = desktop_memory.span.text
        # print(model)
        price = f'{desktop_memory_price.strong.text}{desktop_memory_price.sup.text} $'
        # print(price)
        csv_obj.writerow([model, price])

    sleep(randint(10, 15))