###
# power(x, n) calculates x to the power of n (recursion)
#
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

if __name__ == "__main__":
    print('5^3 =', power(5, 3))
