###
# Calculates the total value of money spent
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, 'r', encoding='utf-8') as file:
    email = file.read()

# regular expression pattern
# for amounts
pattern = r'€\s*\d+(?:[.,]\d+)?|\d+(?:[.,]\d+)?\s*€'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
total = 0
for amount in amounts:
    number = re.findall(r'\d+(?:[.,]\d+)?', amount)[0]
    total += float(number.replace(',', '.'))

# print result
print(f'Total value of money spent: {total:.2f} €')
