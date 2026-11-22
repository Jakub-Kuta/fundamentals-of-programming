###
# f(n) returns the n-th prime number
#
def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True

def f(n):
    found = 0
    candidate = 1
    while found < n:
        candidate += 1
        if is_prime(candidate):
            found += 1
    return candidate

if __name__ == "__main__":
    print('f(1) returns', f(1))
    print('f(5) returns', f(5))
