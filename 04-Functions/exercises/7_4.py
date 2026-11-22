###
# Counts how many times the given letter appears in a text
#
import letters

text = 'You never get a second chance to make a first impression'
letter = 'e'
print(text)
print(f"The number of letter '{letter}': {letters.count_letter(letter, text)}")
