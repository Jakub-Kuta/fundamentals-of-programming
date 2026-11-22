###
# Reverses a text using a stack
#
import queue

def reverse_text(text):
    stack = queue.LifoQueue()
    for char in text:
        stack.put(char)
    result = ''
    while not stack.empty():
        result += stack.get()
    return result

text = input('Enter text: ')
print('Reversed text:', reverse_text(text))
