###
# A program that enables a user to challenge a computer.
# The computer throws dice, the user guesses the number.
#
import random
# COMPUTER TURN
computer = random.randint(1, 6)
# YOUR TURN
you = int(input('Guess the number (1-6): '))
won = computer == you
print(f'Computer rolled: {computer}')
print(f'You won: {won}')
