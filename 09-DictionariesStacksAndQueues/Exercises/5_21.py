###
# Writes data about a favourite movie to the favourite.json file
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import json

favourite = {
    "title": "Fight Club",
    "director": "David Fincher",
    "year": 1999,
    "genre": "Drama",
    "lead_actor": "Brad Pitt",
    "rating": 8.8
}

with open('favourite.json', 'w', encoding='utf-8') as file:
    json.dump(favourite, file, indent=4)

print('Data has been written to favourite.json')
