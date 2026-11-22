###
# Multiplication table 1..10 for a number entered by the user.
#
number = int(input('Enter number: '))
for i in range(1, 11):
    print(f'{number} x {i} = {number * i}')
