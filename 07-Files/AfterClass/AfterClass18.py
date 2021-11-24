file = open("internet.txt","r")
copylines = open("copylines.txt","w")

for line in file:
    copylines.write(line)
    
file.close()
copylines.close()
