###
# f(expression) returns the value of an expression with single-digit
# numbers, addition and subtraction
#
def f(expression):
    result = int(expression[0])
    i = 1
    while i < len(expression):
        operator = expression[i]
        number = int(expression[i + 1])
        if operator == '+':
            result += number
        else:
            result -= number
        i += 2
    return result

if __name__ == "__main__":
    print('f("2+3") returns', f("2+3"))
    print('f("3+8+1") returns', f("3+8+1"))
    print('f("2+3-4+5-0") returns', f("2+3-4+5-0"))
