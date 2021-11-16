a = [1,0,9,6,1]

x = int(input("Enter a number: "))
display = "Numbers that are greater that the number entered: "
for i in a:
    if x<i:
        display+=str(i)+" "

print(display)
