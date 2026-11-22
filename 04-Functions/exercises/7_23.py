###
# f(password) returns True if the password has at least six characters
# and each character appears only once
#
def f(password):
    if len(password) < 6:
        return False
    for char in password:
        if password.count(char) > 1:
            return False
    return True

if __name__ == "__main__":
    print('f("ax15") returns', f("ax15"))
    print('f("book123") returns', f("book123"))
    print('f("A2water3") returns', f("A2water3"))
    print('f("qwerty") returns', f("qwerty"))
    print('f("") returns', f(""))
