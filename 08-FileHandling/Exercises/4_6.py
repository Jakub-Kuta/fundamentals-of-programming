###
# Calculates the number of lines, characters and words in a text file
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_name = input('File name: ')

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    print('File name:', file_name)
    print('Number of lines:', len(content.splitlines()))
    print('Number of characters:', len(content))
    print('Number of words:', len(content.split()))
except FileNotFoundError:
    print(f'File {file_name} does not exist')
except UnicodeDecodeError:
    print(f'File {file_name} cannot be read as a UTF-8 text file')
