###
# Array of dictionaries: countries and their population
#
countries = [
    {"name":"Poland", "population":38000000},
    {"name":"Germany", "population":83000000},
    {"name":"France", "population":68000000},
    {"name":"Spain", "population":48000000},
    {"name":"Italy", "population":59000000}
]

print('COUNTRY  POPULATION')
for country in countries:
    print(f'{country["name"]:<9}{country["population"]}')
