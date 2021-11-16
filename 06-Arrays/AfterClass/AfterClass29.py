array1 = [1,2,3,4]
array2 = [4,5,7,1,2,3]

a=0
b=0
i=0
x=0
while a != len(array1):
    while b != len(array2):
        if array1[a]==array2[b]:
            i+=1
        b+=1
        if i==1:
            x+=1
            i=0
    b=0
    a+=1
if x==len(array1):
    print("All elements of the first array appear in the second array")
else:
    print("Not all elements of the first array appear in the second array")

        