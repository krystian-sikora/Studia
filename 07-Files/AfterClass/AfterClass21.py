file = open("randomintegers.txt","w")
import random

x = random.randint(100,1000)
for number in range(0,50):
    file.write(str(x))
    file.write("\n")
    x = random.randint(100,1000)

file.close()