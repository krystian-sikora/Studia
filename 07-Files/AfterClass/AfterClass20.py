integer_numbers = open("integers.txt","w")
for number in range(1,51):
    integer_numbers.write(str(number))
    integer_numbers.write("\n")
integer_numbers.close()