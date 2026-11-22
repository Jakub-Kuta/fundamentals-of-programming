###
# Converts a natural number to a binary number using a stack
#
import queue

number = int(input('Natural number: '))

stack = queue.LifoQueue()
n = number
if n == 0:
    stack.put(0)
while n > 0:
    stack.put(n % 2)
    n = n // 2

binary = ''
while not stack.empty():
    binary += str(stack.get())

print('Natural number:', number)
print('Binary number:', binary)
