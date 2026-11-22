###
# Finds N leading prime numbers.
#
n = int(input('Enter N: '))
found = 0
candidate = 2
print('Prime numbers:', end=' ')

while found < n:
    is_prime = True
    for divisor in range(2, candidate):
        if candidate % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(candidate, end=' ')
        found += 1
    candidate += 1
print()
