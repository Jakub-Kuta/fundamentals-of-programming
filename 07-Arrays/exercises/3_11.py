###
# Compares two arrays
#
def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

def print_array(label, array):
    print(label, end=' ')
    for value in array:
        print(value, end=' ')
    print()

pairs = [
    (["water","book","sky"], ["water","book","sky"]),
    ([True,False], [True,False,True]),
    ([5,3,1], [5,3,1]),
    ([3,2,1], [3,2])
]

for pair in pairs:
    print_array('Array1:', pair[0])
    print_array('Array2:', pair[1])
    if compare(pair[0], pair[1]):
        print('Comparison: arrays are the same')
    else:
        print('Comparison: arrays are different')
    print()
