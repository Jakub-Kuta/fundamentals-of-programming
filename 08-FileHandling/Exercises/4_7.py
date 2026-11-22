###
# Calculates the number of vowels in a text
#
import re

text = input('Enter text: ')
vowels = re.findall('[aeiouAEIOU]', text)
print('Number of vowels:', len(vowels))
