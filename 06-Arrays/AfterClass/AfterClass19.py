array = [2,3,2,5,8,1,9,8]
display1 = "Unique elements: "
a=0
b=0
i=0
while a != len(array):
    while b != len(array):
        if array[a]==array[b]:
            i+=1
        b+=1
    if i==1:
        display1+=str(array[a])+" "
    i=0
    b=0
    a+=1

print(display1)
    