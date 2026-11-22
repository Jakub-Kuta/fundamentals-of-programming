###
# Seasonal sale: prices reduced by 10%
#
price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

def print_prices(prices):
    total = 0
    for product, price in prices.items():
        print(f'{product}: {price}')
        total += price
    return total

print('Prices before the discount:')
total_before = print_prices(price_list)
print(f'Total value before the discount: {total_before:.2f}')

for product in price_list:
    price_list[product] = round(price_list[product] * 0.9, 2)

print('Prices after the discount:')
total_after = print_prices(price_list)
print(f'Total value after the discount: {total_after:.2f}')
