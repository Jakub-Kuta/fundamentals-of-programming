###
# Functions to operate on an array of numbers (without built-in functions)
#
def second_largest(arr):
    largest = arr[0]
    second = None
    for value in arr:
        if value > largest:
            second = largest
            largest = value
        elif value < largest and (second is None or value > second):
            second = value
    return second

def difference(arr):
    largest = arr[0]
    smallest = arr[0]
    for value in arr:
        if value > largest:
            largest = value
        if value < smallest:
            smallest = value
    return largest - smallest

def median(arr):
    ordered = []
    for value in arr:
        ordered.append(value)
    n = len(ordered)
    for i in range(n):
        for j in range(n - i - 1):
            if ordered[j] > ordered[j+1]:
                z = ordered[j]
                ordered[j] = ordered[j+1]
                ordered[j+1] = z
    if n % 2 == 1:
        return ordered[n // 2]
    return (ordered[n // 2 - 1] + ordered[n // 2]) / 2

def smallest_and_largest(arr):
    largest = arr[0]
    smallest = arr[0]
    for value in arr:
        if value > largest:
            largest = value
        if value < smallest:
            smallest = value
    return [smallest, largest]

def to_string(arr):
    result = ''
    for i in range(len(arr)):
        if i > 0:
            result += '-'
        result += str(arr[i])
    return result
