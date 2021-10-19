# After class
# 19. The length of the sides of the triangle is a, b and c.
# Write a program that calculates the area of the triangle using the Heron formula.
# Read the values of the sides of the triangle from the keyboard.
# Using the program, calculate the area of the triangle for the sides 3, 4 and 5.

a = 3
b = 4
c = 5
p = 1 / 2 * ( a + b + c )
S = ( p * ( p - a ) * ( p - b ) * ( p - c ) ) ** 0.5
print(S)