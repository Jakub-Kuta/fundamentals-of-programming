###
# Simple calculator
#
number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))
operator = input('Enter operator (+, -, *, /): ')
result = None

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    if number2 == 0:
        print('Cannot divide by zero')
    else:
        result = number1 / number2
else:
    print('Incorrect operator')

if result is not None:
    print(f'{number1} {operator} {number2} = {result}')
