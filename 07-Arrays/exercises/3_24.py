###
# Returns a randomly selected array element
#
import random

def rand_elem(array):
    index = random.randint(0, len(array) - 1)
    return array[index]

fruits = ['apple', 'pear', 'plum', 'cherry', 'banana']
for i in range(5):
    print(rand_elem(fruits))
