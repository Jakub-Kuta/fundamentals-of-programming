###
# f(n) returns a string of n asterisks, separated by a slash sign
#
def f(n):
    result = ''
    for i in range(n):
        if i > 0:
            result += '/'
        result += '*'
    return result

if __name__ == "__main__":
    print('f(4) returns', f(4))
    print('f(1) returns', f(1))
