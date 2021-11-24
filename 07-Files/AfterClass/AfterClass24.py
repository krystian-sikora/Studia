import re
with open("forecast.txt","r") as file:
    text = file.read()
    x = re.findall("\d\d",text)
    sum = 0
    how_many_numbers = 0
    for number in x:
        sum+=int(number)
        how_many_numbers+=1

    print(sum/how_many_numbers)