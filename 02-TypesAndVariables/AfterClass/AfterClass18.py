# After class
# 18. In interactive mode, calculate and display your height in feet and inches.
# Sample result: I am 170cm tall, i.e. 5 feet and 7 inches.

heightincm =int(input("Enter your height: "))

# cm to feet ratio = 0.032808399

feet=heightincm*0.032808399

# converting feet to a whole number

feet=int(feet)

# subtracting integer from height because we want to get rid of feet to calculate inches

inches=(heightincm*0.032808399-feet)*12

# converting inches to a whole number

inches=int(inches)

print("I am",heightincm,"cm tall, i.e.",feet,"feet and",inches,"inches.")