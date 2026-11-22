###
# Prints first name, last name and email of graphic designers
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import csv

with open('it_company.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    print('GRAPHIC DESIGNERS')
    print('=================')
    for row in reader:
        if row['Job Title'] == 'Graphic Designer':
            print(f"{row['First Name']} {row['Last Name']},{row['Email']}")
