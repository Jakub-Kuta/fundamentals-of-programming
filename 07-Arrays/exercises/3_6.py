###
# Finds the maximum and minimum number (without built-in functions)
#
arr = [-15, 8, -31, 47, -2, 19]

max_number = arr[0]
min_number = arr[0]
for value in arr:
    if value > max_number:
        max_number = value
    if value < min_number:
        min_number = value

print('Maximum number:', max_number)
print('Minimum number:', min_number)
