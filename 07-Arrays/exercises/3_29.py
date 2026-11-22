###
# Prints the values of a 2x4 array in rows and columns
#
arr = [
    [4, 8, 15, 16],
    [23, 42, 7, 1]
]

for row in arr:
    for value in row:
        print(value, end=' ')
    print()
