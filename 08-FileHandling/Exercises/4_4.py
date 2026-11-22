###
# Prints the file five lines at a time
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('it_company.csv', 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

for i in range(len(lines)):
    print(lines[i])
    if (i + 1) % 5 == 0 and i + 1 < len(lines):
        print('Press Enter key...')
        input()
