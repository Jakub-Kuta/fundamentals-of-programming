###
# f(text) returns the text with all characters separated by a dash
#
def f(text):
    result = ''
    for i in range(len(text)):
        if i > 0:
            result += '-'
        result += text[i]
    return result

if __name__ == "__main__":
    print('f("Univesity") returns', f("Univesity"))
    print('f("UE") returns', f("UE"))
    print('f("x") returns', f("x"))
    print('f("") returns', f(""))
