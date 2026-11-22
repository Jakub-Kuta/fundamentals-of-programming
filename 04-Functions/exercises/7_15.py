###
# f(detector) returns True if at least 3 people were in the room
# at the same time, or False otherwise
#
def f(detector):
    people = 0
    for sign in detector:
        if sign == '+':
            people += 1
        elif sign == '-':
            people -= 1
        if people >= 3:
            return True
    return False

if __name__ == "__main__":
    print('f("+-+++-+---") returns', f("+-+++-+---"))
    print('f("+-+-+-+-") returns', f("+-+-+-+-"))
    print('f("+-++-+--") returns', f("+-++-+--"))
    print('f("+-++-++-+---") returns', f("+-++-++-+---"))
