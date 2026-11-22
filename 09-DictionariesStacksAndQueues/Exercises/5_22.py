###
# Saves data about a purchased product to the product.json file
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import json

product = {}

# read product data from keyboard
product['name'] = input('Product name: ')
product['price'] = round(float(input('Price: ')), 2)
product['paid'] = input('Paid (yes/no): ') == 'yes'

# save product data to json file
with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4)

print('Data has been written to product.json')
