# After class
# 21. Write a program that displays the results of three dice rolls
# and the sum of the dice rolled. Apply a random number generator:
# https://docs.python.org/3/library/random.html

import random
n1 = random.randint(1,6)
n2 = random.randint(1,6)
n3 = random.randint(1,6)
print(f"The number on the first dice is {n1}\nThe number on the second dice is {n2}\nThe number on the third dice is {n3}")
print(f"The sum of the dices rolled is equal to {n1+n2+n3}")