###
# Parking meter: 1-2 h: 5 PLN, 3-6 h: 15 PLN, over 6 h: 20 PLN
#
hours = int(input('Enter number of hours: '))

if hours < 1:
    print('Incorrect number of hours')
elif hours <= 2:
    print('Parking fee: 5 PLN')
elif hours <= 6:
    print('Parking fee: 15 PLN')
else:
    print('Parking fee: 20 PLN')
