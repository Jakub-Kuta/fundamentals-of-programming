###
# Module with a function that counts a letter in a text
#
def count_letter(letter, text):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    return counter
