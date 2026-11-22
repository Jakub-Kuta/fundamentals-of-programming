###
# Prints information about dogs younger than 5 years
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import json

with open('dogs.json', 'r', encoding='utf-8') as file:
    dogs = json.load(file)

for dog in dogs:
    if dog['age'] < 5:
        for key, value in dog.items():
            print(key, ':', value)
        print()
