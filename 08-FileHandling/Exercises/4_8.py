###
# Prints file names whose extensions consist of exactly four characters
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import re

with open('files.txt', 'r', encoding='utf-8') as file:
    for line in file:
        file_name = line.strip()
        if re.search(r'\.\w{4}$', file_name):
            print(file_name)
