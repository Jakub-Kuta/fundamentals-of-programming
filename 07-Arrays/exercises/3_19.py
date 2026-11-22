###
# Counts the number of occurrences of a value in a tuple
#
values = (50, 20, 40, 50, 30, 50)
value = int(input('Value: '))

counter = 0
for item in values:
    if item == value:
        counter += 1

print('Tuple:', end=' ')
for i in range(len(values)):
    if i > 0:
        print(',', end='')
    print(values[i], end='')
print()
print('Value:', value)
print('Number of occurrences:', counter)
