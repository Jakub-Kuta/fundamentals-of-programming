###
# Prints employees employed in a specified position.
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

counter = 1
with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:
        if job_title in line:
            print(f'{counter}. {line}', end="")
            counter += 1
