###
# Summary of hotel reservations
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import json

def read_reservations(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['reservations']

def number_of_rooms(reservations):
    rooms = set()
    for reservation in reservations:
        rooms.add(reservation['room_number'])
    return len(rooms)

def count_paid(reservations, paid):
    counter = 0
    for reservation in reservations:
        if reservation['paid'] == paid:
            counter += 1
    return counter

def total_value(reservations, paid):
    total = 0
    for reservation in reservations:
        if reservation['paid'] == paid:
            total += reservation['nights'] * reservation['price_per_night']
    return total

reservations = read_reservations('reservations.json')

print('Number of rooms:', number_of_rooms(reservations))
print('Number of paid reservations:', count_paid(reservations, True))
print('Number of unpaid reservations:', count_paid(reservations, False))
print(f'Total value of paid reservations: {total_value(reservations, True):.2f}')
print(f'Total value of unpaid reservations: {total_value(reservations, False):.2f}')
