###
# Converts a decimal number into a binary number (division by 2).
#
number = int(input('Enter decimal number: '))
n = number
binary = ''

if n == 0:
    binary = '0'
while n > 0:
    remainder = n % 2
    binary = str(remainder) + binary
    n = n // 2

print(f'{number}(10) = {binary}(2)')
