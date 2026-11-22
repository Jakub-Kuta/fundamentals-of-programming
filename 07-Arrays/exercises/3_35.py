###
# Swaps the first and the last column of a 3x5 array
#
def print_array(arr):
    for row in arr:
        for value in row:
            print(f'{value:3d}', end=' ')
        print()

arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print('Before:')
print_array(arr)

for row in arr:
    z = row[0]
    row[0] = row[len(row) - 1]
    row[len(row) - 1] = z

print('After:')
print_array(arr)
