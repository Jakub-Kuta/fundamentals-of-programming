###
# 25% discount for each product purchased over two.
#
number = int(input('Number of products purchased: '))
price = float(input('Product price: '))

if number > 2:
    amount = 2 * price + (number - 2) * price * 0.75
else:
    amount = number * price

print(f'Amount to pay: {amount:.2f}')
