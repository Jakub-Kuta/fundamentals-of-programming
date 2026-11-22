###
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# Fuel consumption in liters per 100 km: 7, 9 and 6.
#
driving_mode = input('Enter driving mode (A/M/E):')
distance = int(input('Enter distance in km: '))
fuel_consumption = 0

if driving_mode == 'A':
    fuel_consumption = 7 # liters per 100km
elif driving_mode == 'M':
    fuel_consumption = 9
elif driving_mode == 'E':
    fuel_consumption = 6
else:
    print('Incorrect driving mode')

if fuel_consumption > 0:
    total_consumption = distance * fuel_consumption / 100
    print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')
