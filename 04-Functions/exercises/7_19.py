###
# f(number) returns the sum of repeated digits in a number
#
def f(number):
    digits = str(abs(number))
    total = 0
    for digit in digits:
        if digits.count(digit) > 1:
            total += int(digit)
    return total

if __name__ == "__main__":
    print('f(1027) returns', f(1027))
    print('f(230335) returns', f(230335))
    print('f(513553007) returns', f(513553007))
