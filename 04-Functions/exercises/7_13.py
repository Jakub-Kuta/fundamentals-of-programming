###
# f(n) returns numbers from 1 to n as a string
#
def f(n):
    result = ''
    for i in range(1, n + 1):
        result += str(i)
    return result

if __name__ == "__main__":
    print('f(11) returns', f(11))
    print('f(4) returns', f(4))
