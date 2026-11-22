###
# Creates a two dimensional array filled with zeros
#
def create_2d_arr(x, y):
    return [[0 for j in range(y)] for i in range(x)]

arr = create_2d_arr(3, 5)
print(arr)
