###
# f(binary_number) returns True if the given string of digits
# is a valid binary number, or False otherwise
#
def f(binary_number):
    if binary_number == '':
        return False
    for digit in binary_number:
        if digit != '0' and digit != '1':
            return False
    return True

if __name__ == "__main__":
    print('f("101101") returns', f("101101"))
    print('f("1311a10100") returns', f("1311a10100"))
