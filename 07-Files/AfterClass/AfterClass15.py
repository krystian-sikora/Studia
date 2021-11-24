filename = input("Enter the filename: ")
count_lines=0
with open(filename,"r") as file:
    for line in file:
        count_lines+=1
print(f"File name: {filename}")
print(f"Number of lines: {count_lines}")
