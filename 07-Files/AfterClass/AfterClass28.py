import re
with open("grades.txt","r") as file:
    read = file.read()
    grades = re.findall("\d.\d",read)
    sum = 0
    number_of_grades = 0
    for grade in grades:
        sum+=float(grade)
        number_of_grades += 1
    mean = sum/number_of_grades
    print(format(mean,'.2f'))

