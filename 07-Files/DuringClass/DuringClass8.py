file = open("countries.txt", "r")
line_number=0
for line in file:
    line_number+=1
    print(line_number,line,end="")
file.close()