###
# Calculates RPN (Reverse Polish Notation) expressions
#
import queue

stack = queue.LifoQueue()

while True:
    value = input('Enter number, operator (+ - * /) or = : ')

    if value == '=':
        result = stack.get()
        print('Result:', f'{result:g}')
        break
    elif value in ['+', '-', '–', '*', '/']:
        second = stack.get()
        first = stack.get()
        if value == '+':
            stack.put(first + second)
        elif value == '-' or value == '–':
            stack.put(first - second)
        elif value == '*':
            stack.put(first * second)
        else:
            stack.put(first / second)
    else:
        stack.put(float(value))
