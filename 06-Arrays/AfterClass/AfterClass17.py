array1 = [4,36,12,28,9,44,5]
array2 = [5,1,36]
i=0

for a in array1:
    i=0
    for b in array2:
        if a != b:
            i+=1
        if i == len(array2):
            print(a)
