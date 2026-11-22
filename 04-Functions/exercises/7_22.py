###
# f(name) returns the acronym (first letters of all words)
#
def f(name):
    acronym = ''
    for word in name.split():
        acronym += word[0]
    return acronym

if __name__ == "__main__":
    print('f("Internet of Things") returns', f("Internet of Things"))
    print('f("For Your Information") returns', f("For Your Information"))
    print('f("Python") returns', f("Python"))
