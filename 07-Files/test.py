f = open("demofile.txt", "w")
f.write("This file has content now!")
f.close()

f = open("demofile.txt", "r")
print(f.read())
f.close()

import os
os.remove("demofile.txt")

