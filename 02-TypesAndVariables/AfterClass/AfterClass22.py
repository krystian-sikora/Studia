# After class
# 22. Write a program that enables the user to face the computer.
# The computer throws a dice. The user then tries to guess
# the number from a dice by entering a number from 1 to 6 from the keyboard.
# If the user has guessed the number from the dice, the computer displays True.

import random
a = random.randint(1,6)
b = int(input("Guess the number from a dice: "))
print(a==b)