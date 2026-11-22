###
# f(amount_to_pay) returns the minimum number of 1, 2 and 5 PLN coins
#
def f(amount_to_pay):
    coins5 = amount_to_pay // 5
    rest = amount_to_pay % 5
    coins2 = rest // 2
    coins1 = rest % 2
    return coins5 + coins2 + coins1

if __name__ == "__main__":
    print('f(23) returns', f(23))
    print('f(8) returns', f(8))
    print('f(2) returns', f(2))
    print('f(0) returns', f(0))
