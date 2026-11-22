###
# f(x,y) returns the sum of numbers in the range <x,y> that are
# divisible by 2 and 3 and not divisible by 4
#
def f(x, y):
    total = 0
    for i in range(x, y + 1):
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
            total += i
    return total

if __name__ == "__main__":
    print('f(1,20) returns', f(1, 20))
    print('f(10,30) returns', f(10, 30))
