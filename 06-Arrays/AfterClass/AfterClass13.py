array = [8,2,5,1,9]
display1 = "Array: "
display2 = "2nd power: "
a=0
b=0

while a != len(array):
    display1+=str(array[a])+" "
    a+=1

while b !=  len(array):
    display2+=str(array[b]*array[b])+" "
    b+=1
print(display1)
print(display2)