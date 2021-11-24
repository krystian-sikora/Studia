import csv
with open("students.txt","r") as file:
    csv_reader = csv.reader(file,delimiter=',')
    line_count = 0
    for line in csv_reader:
        if line_count == 0:
            line_count+=1
        else:
            print(line[0],line[1],line[4])