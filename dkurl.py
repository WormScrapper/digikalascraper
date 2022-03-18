import json
import requests
import csv
from datetime import date
import time
import random

#add yours here
user_agent_list = [
]


r=requests.get('https://api.digikala.com/v1/search/?has_selling_stock=1&price%5Bmin%5D=20000000&price%5Bmax%5D=1000000000&page=1')
packages_json = r.json()

adddate= date.today()

range1= packages_json['data']['pager']['total_pages'] +1

headerList = ['adddate', 'product_id', 'product_name', 'product_warranty', 'product_url', 'product_brand', 'product_category', 'product_selling_price', 'product_default_price', 'product_lm_min_price' , 'product_seller_name', 'product_seller_page', 'product_seller_age']

with open("ِDK_2_100_mlnt.csv", "a", encoding='utf-8-sig', newline='') as csv_file:
    writer = csv.writer(csv_file)
    #dw= csv.DictWriter(csv_file, delimiter=',', fieldnames=headerList)
    #dw.writeheader()

    for x in range(181,range1) :
        print (x)

        for i in range(1, 4):
            # Pick a random user agent
            user_agent = random.choice(user_agent_list)
            # Set the headers
            headers = {'User-Agent': user_agent}

        newr= requests.get('https://api.digikala.com/v1/search/?has_selling_stock=1&price%5Bmin%5D=20000000&price%5Bmax%5D=1000000000&page=' + str(x), headers=headers)
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

                time.sleep(4)

                writer.writerow([adddate, product_id, product_name, product_warranty , product_url, product_brand , product_category, product_selling_price, product_default_price, product_lm_min_price , product_seller_name, product_seller_page, product_seller_age])


