###
# Saves to a file a list of employees working at a specified position.
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file, 'r', encoding='utf-8') as source:
    with open(position_file, 'w', encoding='utf-8') as target:
        for line in source:
            if job_title in line:
                target.write(line)
