###
# Prints a lottery coupon (numbers from 1 to 49), 7 columns.
#
for row in range(1, 8):
    for col in range(7):
        print(row + col * 7, end=' ')
    print()
