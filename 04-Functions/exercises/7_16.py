###
# f(n) returns the n-th value of the Fibonacci sequence
#
def f(n):
    a = 0
    b = 1
    for i in range(n - 1):
        c = a + b
        a = b
        b = c
    return a

if __name__ == "__main__":
    print('f(5) returns', f(5))
    print('f(9) returns', f(9))
