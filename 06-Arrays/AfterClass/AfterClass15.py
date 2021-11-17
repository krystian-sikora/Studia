colors = ["red", "green", "blue"]
f = open("colors.txt", "w")
for color in colors:
    f.write(color)
    f.write("\n")
f.close()
f = open("colors.txt", "r")
print(f.read())
f.close()
