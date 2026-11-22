###
# Uses the functions from the MyArrays module
#
import MyArrays

numbers = [7, 3, 8, 5, 2]

print('Numbers:', end=' ')
for i in range(len(numbers)):
    if i > 0:
        print(',', end='')
    print(numbers[i], end='')
print()

print('Second largest number:', MyArrays.second_largest(numbers))
print('Difference between the largest and smallest number:', MyArrays.difference(numbers))
print('Median:', MyArrays.median(numbers))
result = MyArrays.smallest_and_largest(numbers)
print(f'Smallest and largest number: {result[0]},{result[1]}')
print('Numbers as a string:', MyArrays.to_string(numbers))
