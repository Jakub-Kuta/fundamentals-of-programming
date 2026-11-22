###
# Checks if a number is within the range <x, y>
#
import ranges

number = int(input('A number: '))
x = 2
y = 15
if ranges.in_range(number, x, y):
    answer = 'yes'
else:
    answer = 'no'
print(f'Number {number} in the range <{x},{y}>: {answer}')
