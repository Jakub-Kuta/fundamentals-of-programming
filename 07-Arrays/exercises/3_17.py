numbers = (10, 20, 30, 40, 50)

print('Tuple:', end=' ')
for i in range(len(numbers)):
    if i > 0:
        print(',', end='')
    print(numbers[i], end='')
print()

print('Reverse order:', end=' ')
for i in range(len(numbers) - 1, -1, -1):
    if i < len(numbers) - 1:
        print(',', end='')
    print(numbers[i], end='')
print()
