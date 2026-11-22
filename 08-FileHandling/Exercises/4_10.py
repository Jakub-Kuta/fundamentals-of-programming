###
# Prints products with price less than 60 and stock less than 40
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import csv

with open('clothing.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if float(row['Price']) < 60 and int(row['Stock_Quantity']) < 40:
            print(', '.join(row.values()))
