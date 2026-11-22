###
# f(product_code) returns True if the product code is correct:
# the fourth digit is the remainder of dividing the sum
# of the first three digits by 7
#
def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit():
        return False
    total = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    return total % 7 == int(product_code[3])

if __name__ == "__main__":
    print('f("1082") returns', f("1082"))
    print('f("2035") returns', f("2035"))
    print('f("1114") returns', f("1114"))
    print('f("7071") returns', f("7071"))
