###
# Yes-no survey, answers saved in logical (bool) variables.
#
print('SURVEY')
computer_science = input('Are you interested in computer science? (y/n): ') == 'y'
games = input('Do you like playing computer games? (y/n): ') == 'y'
instagram = input('Do you have an Instagram account? (y/n): ') == 'y'

print()
print('SURVEY RESULTS')
print(f'Interested in computer science: {"Yes" if computer_science else "No"}')
print(f'Playing computer games: {"Yes" if games else "No"}')
print(f'Has an Instagram account: {"Yes" if instagram else "No"}')
