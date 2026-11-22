###
# Puts all even numbers first, and then odd numbers
#
arr = [7, 9, 2, 4, 5, 6]
print('arr =', arr)

evens = []
odds = []
for number in arr:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)
arr = evens + odds

print('arr =', arr)
