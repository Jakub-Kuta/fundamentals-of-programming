###
# Displays the Euro exchange rates from the euro.json file
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import json

with open('euro.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print('Date            Buying Rate     Selling Rate')
print('============================================')
for rate in data['rates']:
    print(f'{rate["effectiveDate"]:<16}{rate["bid"]:<16.4f}{rate["ask"]:.4f}')
