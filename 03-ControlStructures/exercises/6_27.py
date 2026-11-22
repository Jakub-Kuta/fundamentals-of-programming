###
# Numeric keyboard - version with while instead of for.
#
# Oryginal:
# for i in range(6,-1,-3):          # i = 6, 3, 0
#     for j in range(1,4):          # j = 1, 2, 3
#         print(f'{i+j}',end=' ')
#     print()

i = 6
while i >= 0:
    j = 1
    while j <= 3:
        print(f'{i+j}', end=' ')
        j += 1
    print()
    i -= 3
