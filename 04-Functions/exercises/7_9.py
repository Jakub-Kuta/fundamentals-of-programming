###
# f(number, even) returns the sum of the even digits (even=True)
# or the sum of the odd digits (even=False) of a number
#
def f(number, even):
    total = 0
    for digit in str(abs(number)):
        value = int(digit)
        if (value % 2 == 0) == even:
            total += value
    return total

if __name__ == "__main__":
    print('f(3124,True) returns', f(3124, True))
    print('f(3124,False) returns', f(3124, False))
    print('f(20576,False) returns', f(20576, False))
    print('f(20576,True) returns', f(20576, True))
    print('f(13115,True) returns', f(13115, True))
