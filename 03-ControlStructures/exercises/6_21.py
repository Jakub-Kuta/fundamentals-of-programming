###
# Shows an amount with as few coins (5, 2, 1 PLN) as possible.
#
amount = int(input('Enter the amount in PLN: '))

coins5 = amount // 5
rest = amount % 5
coins2 = rest // 2
coins1 = rest % 2

print(f'The amount of PLN {amount} in coins:')
print(f'5 PLN coins: {coins5}')
print(f'2 PLN coins: {coins2}')
print(f'1 PLN coins: {coins1}')
