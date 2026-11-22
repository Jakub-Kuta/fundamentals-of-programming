###
# Calculates, prints and saves to a file integers from 1 to 100
# and their second and third powers
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('powers.txt', 'w') as file:
    for i in range(1, 101):
        line = f'{i},{i**2},{i**3}'
        print(line)
        file.write(line + '\n')
