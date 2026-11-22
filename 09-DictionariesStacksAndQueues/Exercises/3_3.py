###
# Checks if the brackets are used correctly in an expression
#
import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    stack = queue.LifoQueue()
    pairs = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in '({[':
            stack.put(char)
        elif char in ')}]':
            if stack.empty():
                return False
            opening = stack.get()
            if opening != pairs[char]:
                return False
    return stack.empty()

if brackets_ok(expression1):
    print(expression1, '- brackets ok')
else:
    print(expression1, '- brackets not correct')

if brackets_ok(expression2):
    print(expression2, '- brackets ok')
else:
    print(expression2, '- brackets not correct')

if brackets_ok(expression3):
    print(expression3, '- brackets ok')
else:
    print(expression3, '- brackets not correct')
