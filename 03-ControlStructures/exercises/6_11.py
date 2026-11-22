###
# Buy recommendation when price dropped by at least 10%
#
current_price = 140.00
previous_price = 200.00
print(f'Current product price: {current_price:.2f}')
print(f'Previous product price: {previous_price:.2f}')

reduction_percent = (previous_price - current_price) * 100 / previous_price
if reduction_percent >= 10:
    print('Buy the product!!')
    print(f'Product price reduced by {reduction_percent:.0f}%')
