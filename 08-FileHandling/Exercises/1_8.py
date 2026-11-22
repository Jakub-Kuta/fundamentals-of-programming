###
# Prints the text from the file and counts the number of words
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

total_words = 0
with open('pets.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line, end="")
        total_words += len(line.split())

print()
print('Number of words:', total_words)
