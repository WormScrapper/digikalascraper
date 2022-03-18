import json
import requests
import csv
from datetime import date
import time
import random

user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

r=requests.get('https://api.digikala.com/v1/incredible-offers/products/?page=1')
packages_json = r.json()

headers=r.request.headers

adddate= date.today()

range1= packages_json['data']['pager']['total_pages'] +1

headerList = ['adddate', 'product_id', 'product_name', 'product_warranty', 'product_url', 'product_brand', 'product_category', 'product_selling_price', 'product_default_price', 'product_lm_min_price' , 'product_seller_name', 'product_seller_page', 'product_seller_age']

with open("ِDK_Amazing.csv", "a", encoding='utf-8-sig', newline='') as csv_file:
    writer = csv.writer(csv_file)
    #dw= csv.DictWriter(csv_file, delimiter=',', fieldnames=headerList)
    #dw.writeheader()

    for x in range(1,range1) :

        for i in range(1, 4):
            # Pick a random user agent
            user_agent = random.choice(user_agent_list)
            # Set the headers
            headers = {'User-Agent': user_agent}

        newr= requests.get('https://api.digikala.com/v1/incredible-offers/products/?page=' + str(x), headers=headers)
        package_json = newr.json()
        range2 = len(package_json['data']['products'])
        for x in range(range2) :
            if package_json['data']['products'][x]['status'] == "marketable" :

                try:
                    product_selling_price = int((package_json['data']['products'][x]['default_variant']['price']['selling_price'])/10)
                    product_default_price = int((package_json['data']['products'][x]['default_variant']['price']['rrp_price'])/10)
                    product_lm_min_price = int((package_json['data']['products'][x]['properties']['min_price_in_last_month'])/10)
                except:
                    product_selling_price = 0
                    product_default_price = 0
                    product_lm_min_price = 0

                product_name = package_json['data']['products'][x]['title_fa']
                product_id = 'DKP-' + str(package_json['data']['products'][x]['id'])
                product_brand = package_json['data']['products'][x]['data_layer']['brand']
                product_category = package_json['data']['products'][x]['data_layer']['category']
                product_seller_name = package_json['data']['products'][x]['default_variant']['seller']['title']
                product_seller_page = package_json['data']['products'][x]['default_variant']['seller']['url']
                product_seller_age = package_json['data']['products'][x]['default_variant']['seller']['registration_date']
                product_warranty = package_json['data']['products'][x]['default_variant']['warranty']['title_fa']
                product_url = 'www.digikala.com' + str(package_json['data']['products'][x]['url']['uri'])

                time.sleep(3)

                writer.writerow([adddate, product_id, product_name, product_warranty , product_url, product_brand , product_category, product_selling_price, product_default_price, product_lm_min_price , product_seller_name, product_seller_page, product_seller_age])


