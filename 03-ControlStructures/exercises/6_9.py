###
# Prints the name if it is a Polish female name (ends with 'a')
#
name = input('Enter name: ')
if name[-1].lower() == 'a':
    print(f'{name} -- Polish female name')
