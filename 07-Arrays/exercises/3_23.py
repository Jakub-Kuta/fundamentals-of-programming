###
# Checks whether the first array is a subset of the second one
#
def is_subset(array1, array2):
    for value in array1:
        if value not in array2:
            return False
    return True

array1 = [3, 5, 7]
array2 = [1, 3, 5, 7, 9]
print(array1, array2, is_subset(array1, array2))

array1 = [3, 4]
print(array1, array2, is_subset(array1, array2))
