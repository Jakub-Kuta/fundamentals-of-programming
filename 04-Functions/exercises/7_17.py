###
# f(palindrome) returns True if the expression is a palindrome
#
def f(palindrome):
    n = len(palindrome)
    for i in range(n // 2):
        if palindrome[i] != palindrome[n - 1 - i]:
            return False
    return True

if __name__ == "__main__":
    print('f("radar") returns', f("radar"))
    print('f("12-11-21") returns', f("12-11-21"))
    print('f("book") returns', f("book"))
