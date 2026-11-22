###
# Bubble sort
#
def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                z = array[j]
                array[j] = array[j+1]
                array[j+1] = z
    return array

array1 = [5, 2, 9, 1, 7]
array2 = [10, -3, 8, 0, 4, -7]
array3 = [3.5, 1.2, 9.9, 2.8]

for array in [array1, array2, array3]:
    print('Before:', array)
    print('Sorted:', bubblesort(array))
