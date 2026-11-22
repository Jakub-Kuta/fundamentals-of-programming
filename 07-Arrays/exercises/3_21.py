###
# Prints the number of elements greater than a value from the keyboard
#
arr = [3.5, 7.2, 1.1, 9.8, 4.4, 6.0, 2.7]
value = float(input('Enter a value: '))

counter = 0
for number in arr:
    if number > value:
        counter += 1

print('Array:', arr)
print(f'Number of elements greater than {value}: {counter}')
