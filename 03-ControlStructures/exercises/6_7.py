###
# Age group: Child (<13), Teen (13-19), Adult (20-64), Senior (65+)
#
age = int(input('Enter your age: '))

if age < 13:
    print('Child')
elif age <= 19:
    print('Teen')
elif age <= 64:
    print('Adult')
else:
    print('Senior')
