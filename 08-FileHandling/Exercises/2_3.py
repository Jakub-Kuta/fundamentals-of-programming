###
# Makes a copy of a text file
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file, 'r', encoding='utf-8') as file:
    content = file.read()

# write the content to the target file (copy)
with open(target_file, 'w', encoding='utf-8') as file:
    file.write(content)
