###
# Counts how many registered cars come from each province of Poland
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import csv

# letter --> province
provinces = {}
with open('province.csv', 'r', encoding='utf-8', newline='') as file:
    for row in csv.DictReader(file):
        provinces[row['Letter']] = row['Name']

# province --> number of cars
counts = {}
with open('vehicle.txt', 'r', encoding='utf-8') as file:
    for line in file:
        car_number = line.strip()
        if car_number != '':
            letter = car_number[0]
            if letter in provinces:
                province = provinces[letter]
                if province in counts:
                    counts[province] += 1
                else:
                    counts[province] = 1

for province, count in counts.items():
    print(f'{province}: {count}')
