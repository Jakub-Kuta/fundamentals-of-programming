###
# Records voting in the voting.json file
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import json

# Read the contents of the json file
try:
    with open('voting.json', 'r', encoding='utf-8') as file:
        votes = json.load(file)
except FileNotFoundError:
    votes = {}

# Vote for a person
person_name = input('Name of the person you are voting for:')
if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1

# Save voting data to json file
with open('voting.json', 'w', encoding='utf-8') as file:
    json.dump(votes, file, indent=4)

for name, number in votes.items():
    print(f'{name}: {number}')
