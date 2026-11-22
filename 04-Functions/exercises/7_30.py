###
# sum_natural(n) calculates the sum of natural numbers from 1 to n
# (recursion)
#
def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

if __name__ == "__main__":
    print('The sum of natural numbers in the range <1,10> is', sum_natural(10))
