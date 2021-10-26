a=int(input("Enter a: "))
b=int(input("Enter b: "))

print("*"*b)
for x in range(1,a-1):
    print("*"," "*(b-4),"*")
print("*"*b)